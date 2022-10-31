import openai
from data import Const

with open(r"apikey/api_secrets.txt", "r") as file:
    openai.api_key = file.readline()


class GPT3():
    MAX_CONVO_MESSAGES = 20  # 最後の20メッセージだけを呼び出す

    convo_message_prompt = f"以下は、{Const.MyName}という日本語で答えるAIとの会話です.{Const.MyName}は、親切で、創造的で、賢くて、人と話すのが好きで、とてもフレンドリーです.\n\n"
    # \nHuman: 好きな食べ物は何ですか.\nAI: 私は寿司がとても好きです！魚が甘くておいしいです!
    def conversation(self, input_messages=None):
        # input_message_str = self.convo_message_prompt + input_messages + "\n"
        input_message_str = self.convo_message_prompt + \
            "\n".join(input_messages[-self.MAX_CONVO_MESSAGES:]) + "\n"
        response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=input_message_str,
            temperature=0.8,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        try:
            res_text = response['choices'][0]['text']
            # 出力から無駄な情報(AI: や Human:)を抜きたい
            last_response = res_text.replace("AI:", "").replace(
                "Human:", "").replace(f"{Const.MyName}:", "").strip()
        except Exception:
            return input_messages, None

        return input_messages, last_response


# Special Variable Python to "execute following code only if this file is run as a script from the command line".
if __name__ == "__main__":
    msginput = "好きな映画は何ですか？"
    input, last = GPT3().conversation([msginput])
    print(last)
