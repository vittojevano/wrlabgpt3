from gptsys import GPTSystem, GetRespondState

class SysInfo(object):
    Idle = "Idle"
    Engaging = "Engaging"
    Conversing = "Conversing"

# Check if we can use it in the robot
class SysState(object):
    # If the person is invisible for 6 sec, go to Idle mode
    TimeToDisengage = 6
    # If the person is visible for 2 sec, start talking
    TimeToConverse = 2

    def __init__(self):
        self._state = SysInfo.Idle
        self._gptsys = GPTSystem() # Intent
        # self._person = None
        self._stop_watch = None
        # self._disengaged_stop_watch = None

    def sysrun(self):
        self._gptsys.start_listening()
        
        # Pool thought module to hear what the human said and to generate respond from GPT3
        get_respond_state, respond_message = self._gptsys.get_respond()

        if get_respond_state == GetRespondState.HearingTimeOut:
            # Did not hear from human, remove last conversation from record.
            self._gptsys.remove_last_conversation()
            print("Not Recorded.")
        elif get_respond_state == GetRespondState.GPT3TimeOut:
            # Got GPT3 Issue. Remove last conversation.
            self._gptsys.remove_last_conversation()
            print("GPT3 Error, please state again")
        elif get_respond_state == GetRespondState.Completed:
            if respond_message is not None and len(respond_message)>0:
                print("AI:",respond_message)

    def _reset(self):
        # Stop listening
        self._gptsys.reset()