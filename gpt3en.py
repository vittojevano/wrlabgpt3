import openai
from data import Const

with open(r"apikey/api_secrets.txt", "r") as file:
    openai.api_key = file.readline()


class GPT3(object):
    MAX_CONVO_MESSAGES = 20  # 最後の20メッセージだけを呼び出す
    convo_message_prompt = "The following is a conversation with an AI named PALRO. PALRO is talkative, clever, friendly, and likes to talk with humans.\n\nHuman: Let's talk about food. What food do you like?\nAI: I like sushi a lot! It tasted sweet and yummy!\nHuman: How about sports? Are you Interested in sports?\nAI: Yes! I really like basketball and soccer!\n"
    # convo_message_prompt = f"The following is a conversation with an AI called {Const.MyName}. {Const.MyName} is helpful, creative, clever, likes to talk to people, and very friendly.\n\n"
    # \nHuman: What food do you like?\nAI: I like sushi a lot! It tasted sweet and yummy!
    def conversation(self, input_messages=None):
        # input_message_str = self.convo_message_prompt + input_messages + "\n"
        input_message_str = self.convo_message_prompt + \
            "\n".join(input_messages[-self.MAX_CONVO_MESSAGES:]) + "\n"
        engine = 'text-curie-001'
        response = openai.Completion.create(
            engine=engine,
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
'''if __name__ == "__main__":
    text = "Who is your favorite actor?"
    # transtext = tr().transen(text)
    input, last = GPT3().conversation([text])
    print("AI: " + last)
    # response = tr().transjp(last)
    # print(response)'''