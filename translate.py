import deepl

#　APIキーを読み取る
with open(r"apikey/apideepl.txt", "r") as file:
    auth_key = file.readline()

# APIキーの確認
translator = deepl.Translator(auth_key)


class Deepltranslate():

    #　元々の言語から英語に翻訳
    def transen(self, text):
        result = translator.translate_text(text, target_lang="EN-US")

        return str(result)

    #　元々の言語から日本語に翻訳
    def transjp(self, text):
        result = translator.translate_text(text, target_lang="JA")

        return str(result)


# このファイルをコマンドラインからスクリプトとして実行した場合のみ、以下のコードを実行する
if __name__ == "__main__":
    text = "好きな映画は何ですか？"
    response = Deepltranslate().transen(text)
    print(response)
