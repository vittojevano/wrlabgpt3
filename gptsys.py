import os
import random
import threading

from googlestt import GoogleSTT
from gpt3en import GPT3
from translate import Deepltranslate
from timeset import Timeset


class GetRespondState():
    Idle = "Idle"
    Listening = "Listening"
    WaitingForGPT3 = "WaitingForGPT3"
    HearingTimeOut = "HearingTimeOut"
    GPT3TimeOut = "GPT3TimeOut"
    Completed = "Completed"


class GPTSystem():

    HumanPrefix = "Human"

    ListeningTimeOut = 10
    Gpt3TimeOut = 5

    def __init__(self):
        self._conversations = []
        self._googlestt = GoogleSTT()  # thoughts
        self._gpt = GPT3()  # hearing
        self._translate = Deepltranslate()  # deepl
        self._respond_state = GetRespondState.Idle
        self._last_gpt3_response = None
        self._gpt3_call_completed = False
        self._stop_watch = Timeset()

    def speak(self, text, text_translated, record=True):
        print(f"AI:{text_translated}")
        self._googlestt.stop_listening()

        # Record what the AI said
        if record:
            self._conversations.append(f"AI:{text}")
            # print("\n".join(self._conversations))

    def start_listening(self):
        self._googlestt.start_listening()

    def stop_listening(self):
        self._googlestt.stop_listening()

    def get_respond(self):
        respond_message = None
        respond_message_translated = None

        # Start the state machine if the state was idle or previously completed/timeout
        if self._respond_state in [GetRespondState.Idle, GetRespondState.GPT3TimeOut, GetRespondState.HearingTimeOut, GetRespondState.Completed]:
            self.start_listening()
            # Problem, sometimes doesnt stop hearing
            self._respond_state = GetRespondState.Listening
            self._stop_watch = Timeset()
        elif self._respond_state == GetRespondState.Listening:
            # Pool the hearing module to get the last heard message
            last_heard_message = self._googlestt.get_last_speech_message()

            # Got message
            if last_heard_message is not None and len(last_heard_message) > 0:
                print(f"Human:{last_heard_message}")
                self.stop_listening()

                # Record message
                # Translate to english language
                last_heard_message = self._translate.transen(
                    last_heard_message)
                self._conversations.append(
                    f"{self.HumanPrefix}:{last_heard_message}")

                self._respond_state = GetRespondState.WaitingForGPT3
                self._gpt3_call_completed = False
                self._last_gpt3_response = None
                self._stop_watch = Timeset()

                # Pass the convo history to GPT3 to generate responds
                # Generate random request id and keep it for request cancellation
                self._last_request_id = random.random()
                self._thread = threading.Thread(
                    target=self._callback, args=(self._last_request_id,))
                self._thread.daemon = False
                self._thread.start()
            else:
                # Keep listening until timeout
                duration = self._stop_watch.get() / 1000

                if duration >= self.ListeningTimeOut:
                    self._respond_state = GetRespondState.HearingTimeOut

        elif self._respond_state == GetRespondState.WaitingForGPT3:
            if self._gpt3_call_completed:
                # Reset the state back to idle
                self._respond_state = GetRespondState.Completed
                # Return the GPT3 response:
                respond_message = self._last_gpt3_response
                # Translate back to Japanese
                respond_message_translated = self._translate.transjp(
                    respond_message)
            else:
                # Keep waiting until timeout
                duration = self._stop_watch.get() / 1000

                if duration >= self.Gpt3TimeOut:
                    self._respond_state = GetRespondState.GPT3TimeOut

        return self._respond_state, respond_message, respond_message_translated

    def reset(self):
        self.stop_listening()
        self._respond_state = GetRespondState.Idle
        # Reset conversation
        self._conversations = []

    def _callback(self, request_id):
        full_conversations, last_response = self._gpt.conversation(
            self._conversations)

        # Only return the response if the last request id is ours. Otherwise, another request might be
        # running and let it be the one to return the response
        if self._last_request_id == request_id:
            # Record the response and signal the main thread that we are completed
            self._last_gpt3_response = last_response
            self._gpt3_call_completed = True
            self._last_request_id = None

    def remove_last_conversation(self):
        self._conversations = self._conversations[:-1]
