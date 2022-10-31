import deepl

with open(r"apikey/apideepl.txt", "r") as file:
    auth_key = file.readline()

translator = deepl.Translator(auth_key)


class Deepltranslate():

    def transen(self, text):
        result = translator.translate_text(text, target_lang="EN-US")

        return str(result)

    def transjp(self, text):
        result = translator.translate_text(text, target_lang="JA")

        return str(result)


if __name__ == "__main__":
    text = "好きな映画は何ですか？"
    response = Deepltranslate().transen(text)
    print(response)
