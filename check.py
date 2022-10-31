class Test():
    def __init__(self):
        self._text = "会話終了"

    def main(self):
        if self._text == "会話終了":
            print("close")
        else:
            print("error")

if __name__ == "__main__":
    Test().main()