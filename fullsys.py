import time
import math

from gptsys import GPTSystem, GetRespondState
from translate import Deepltranslate

"""
ここからのコードはロボットの機能と動作と一緒に動作する
"""


class SysState(object):

    def __init__(self):
        self._gptsys = GPTSystem()
        self._translate = Deepltranslate()
        self._stop_watch = None

    def question(self, text):
        textjp = self._translate.transjp(text)
        self._gptsys.speakonly(textjp)
        timeextra = math.floor(len(textjp)/17)*3
        totaltime = 7 + timeextra
        # print("time to wait :" + str(totaltime) + "seconds")
        time.sleep(totaltime)
        print("話してOKだよ！")

    def appendai(self):
        self._gptsys.append_ai()

    def sysrun(self):
        # self._gptsys.start_listening()

        # GPT3からの応答を聞き、文章を生成するためのプール思考モジュール
        get_respond_state, respond_message, respond_message_translated = self._gptsys.get_respond()

        if get_respond_state == GetRespondState.GooglesttTimeOut:
            # 人間から連絡がない、最後の会話を記録から削除する。
            self._gptsys.speak("Please speak again",
                               "すみません、あなたの声が聞こえません。もう一度お願いします。", record=False)
            # print("time to wait : 8 seconds")
            time.sleep(8)
            print("話してOKだよ！")
        elif get_respond_state == GetRespondState.GPT3TimeOut:
            # GPT3の問題が発生した場合、最後の会話を削除します。
            self._gptsys.remove_last_conversation()
            self._gptsys.speak("GPT3 Error, please state again",
                               "すみません、ちょっと考えがまとまりません。もう一度お願いします。", record=False)
            # print("time to wait : 8 seconds")
            time.sleep(8)
            print("話してOKだよ！")
        elif get_respond_state == GetRespondState.Completed:
            if respond_message is not None and len(respond_message) > 0:
                self._gptsys.speak(
                    respond_message, respond_message_translated)
                timeextra = math.floor(len(respond_message_translated)/17)*3
                totaltime = 7 + timeextra
                # print("time to wait :" + str(totaltime) + "seconds")
                time.sleep(totaltime)
                print("話してOKだよ！")

    def _reset(self):
        # 聞くのをやめる
        self._gptsys.reset()
