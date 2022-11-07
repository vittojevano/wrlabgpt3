import os
import threading

import pyaudio
from google.cloud import speech
from six.moves import queue

# APIキーの読み取りと確認
Cloud_KEY = "apikey/Cloud_KEY.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Cloud_KEY

# 音声記録パラメータ
RATE = 44100
CHUNK = int(RATE / 10)  # 100ms


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,

            channels=1,
            rate=self._rate,
            input_device_index=0,
            input=True,
            frames_per_buffer=self._chunk,

            stream_callback=self._fill_buffer,
        )
        # 初めて起動するときに音声をに聞かない
        self._listening = False
        self.closed = False
        # print("ここはenter")

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def setListening(self, listen):
        self._listening = listen

    def isListening(self):
        return self._listening

    def generator(self):
        # print("ここはgenerator")
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return

            if not self._listening:
                # print("listeningの状態出ない場合は続く")
                continue

            data = [chunk]

            # まだバッファリングされている他のデータを全て処理する。
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


class SpeechInputRecognitionStreaming(object):

    def __init__(self):
        self._language_supports = "ja-JP"  # 日本語を受け取るに設定
        self.ready = False
        self._stream = None

    def _listenPrintLoop(self, responses, callback, stream):
        """Iterates through server responses and prints them.
        The responses passed is a generator that will block until a response
        is provided by the server.
        Each response may contain multiple results, and each result may contain
        multiple alternatives; for details, see hC;ttps://goo.gl/tjCPAU.  Here we
        print only the transcription for the top alternative of the top result.
        In this case, responses are provided for interim results as well. If the
        response is an interim one, print a line feed at the end of it, to allow
        the next result to overwrite it, until the response is a final one. For the
        final one, print a newline to preserve the finalized transcription.
        """
        num_chars_printed = 0
        for response in responses:
            if not response.results:
                continue

            # the `results` list is consecutive. For streaming, we only care about
            # the first result being considered, since once it's `is_final`, it
            # moves on to considering the next utterance.
            result = response.results[0]
            if not result.alternatives:
                continue

            # Display the transcription of the top alternative.
            transcript = result.alternatives[0].transcript

            # Display interim results, but with a carriage return at the end of the
            # line, so subsequent lines will overwrite them.
            #
            # If the previous result was longer than this one, we need to print
            # some extra spaces to overwrite the previous result
            overwrite_chars = " " * (num_chars_printed - len(transcript))

            if not result.is_final:
                # sys.stdout.write(transcript + overwrite_shars + '\r')
                # sys.stdout.flush()

                num_chars_printed = len(transcript)

            else:
                finaltext = transcript + overwrite_chars

                # 話す途中に聞かない
                # stream.setListening(False)

                if stream.isListening():
                    if callback(finaltext, result.language_code):
                        break
                # stream.setListening(True)

                # 今は聞いていい

                num_chars_printed = 0

    def set_listening(self, is_listening):
        if not self.ready:
            # readyがTrueになるまでに待つ。
            time = threading.Timer(3.0, self.set_listening, [is_listening])
            time.start()
        else:
            self._stream.setListening(is_listening)

    def is_listening(self):
        if self.ready:
            return self._stream.isListening()
        else:
            return False

    def listen_forever(self, callback):
        while True:
            language_code = self._language_supports
            # alternative_language_codes = []
            #
            # if len(self._language_supports) > 1:
            #   alternative_language_codes = self._language_supports[1:]

            # CHECK HERE!!!
            client = speech.SpeechClient()
            # client = speech.SpeechClient
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=RATE,
                language_code=language_code,
                enable_automatic_punctuation=True
                # alternative_language_codes=alternative_language_codes
            )
            streaming_config = speech.StreamingRecognitionConfig(
                config=config,
                interim_results=True)

            with MicrophoneStream(RATE, CHUNK) as stream:
                self._stream = stream
                audio_generator = stream.generator()
                requests = (speech.StreamingRecognizeRequest(audio_content=content)
                            for content in audio_generator)

                self.ready = True

                # ここのエラーを無視してください(実際はエラーではない)
                responses = client.streaming_recognize(
                    streaming_config, requests)

                try:
                    self._listenPrintLoop(responses, callback, stream)
                    break
                except Exception as ex:
                    # Most Likely stream too long Exception, so just log and restart
                    print(ex)
                    pass
