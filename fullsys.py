from gptsys import GPTSystem, GetRespondState


class SysInfo(object):
    Idle = "Idle"
    Engaging = "Engaging"
    Conversing = "Conversing"


"""
ここからのコードはロボットの機能と動作と一緒に動作する
"""


class SysState(object):
    # 人が見えない状態が6秒間続くと、Idleモードに移行する
    TimeToDisengage = 6
    # 2秒間、人が見えたら、話し始める
    TimeToConverse = 2

    def __init__(self):
        self._state = SysInfo.Idle
        self._gptsys = GPTSystem()
        # self._person = None
        self._stop_watch = None
        # self._disengaged_stop_watch = None

    def sysrun(self):
        self._gptsys.start_listening()

        # GPT3からの応答を聞き、文章を生成するためのプール思考モジュール
        get_respond_state, respond_message, respond_messsage_translated = self._gptsys.get_respond()

        if get_respond_state == GetRespondState.HearingTimeOut:
            # 人間から連絡がない、最後の会話を記録から削除する。
            self._gptsys.speak("Please speak again",
                               "すみません、あなたの声が聞こえません。もう一度お願いします。", record=False)
        elif get_respond_state == GetRespondState.GPT3TimeOut:
            # GPT3の問題が発生した場合、最後の会話を削除します。
            self._gptsys.remove_last_conversation()
            self._gptsys.speak("GPT3 Error, please state again",
                               "すみません、ちょっと考えがまとまりません。もう一度お願いします。", record=False)
        elif get_respond_state == GetRespondState.Completed:
            if respond_message is not None and len(respond_message) > 0:
                self._gptsys.speak(
                    respond_message, respond_messsage_translated)

    def _reset(self):
        # 聞くのをやめる
        self._gptsys.reset()
