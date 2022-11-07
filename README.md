# GPT-3, DeepL, and Google STT API for Robot System

DISCLAIMER: This is only for research and personal use only. There won't be any English version of this readme.

Main Reference: *[Building Ellee — A GPT-3 and Computer Vision-Powered Talking Robotic Teddy Bear With Human-Level Conversation Intelligence](https://towardsdatascience.com/building-ellee-a-gpt-3-and-computer-vision-powered-talking-robotic-teddy-bear-with-human-level-db7d08259583)*

@2022, Vitto Jevano Christiant
***


### 1. OpenAI GPT-3
1.1 GPT-3とは
<p> &nbsp;&nbsp;&nbsp;&nbsp;GPT-3は「Generative Pre-trained Transformer - 3」の略で、OpenAIが開発した事前学習済み（Pre-trained）の文章生成型（Generative）の自然言語処理向けの深層学習モデル「Transformer」、その3番目のモデルを指します。つまり、GPTはTransformerという学習モデルをベースにして、しっかりと事前学習を行い文章生成を行うようにカスタマイズされたAI（言語モデル）ということになります。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;GPT-3は基本的にすべての文章はそれぞれの関係性の一部として理解されます。単語や文章の意味、知識の扱い方については考えておらず、単純に「今日はいい天気ですね」と関係性の深い文章を探し、その次に並べるといった仕組みで運用されます。シンプルですが、シンプルであるがゆえに複雑で膨大なデータであっても扱えますし、応用も簡単です。</p>

![gpt3ex](https://user-images.githubusercontent.com/88228805/200279485-a8e993c1-4de1-4e86-b75b-78d5ee4fca31.jpg)
<p align="center">図1&nbsp;&nbsp;&nbsp;&nbsp;GPT-3の自然言語処理「Word to Vector」（言葉をベクトル化する）</p>

参考文献= *[ビジネス+IT](https://www.sbbit.jp/article/cont1/74706)* (参照 2022-11-7)

1.2 GPT-3の使い方

1. OpenAIのURLを開く: https://openai.com/api/
2. Sign Upをクリックする。
3. アカウントを作成する。電話番号の登録が必要なのでご注意ください。
4. APIキーを設定する。
<p> &nbsp;&nbsp;&nbsp;&nbsp;APIキーはログインした後に右上の「Personal」から「View API Keys」をクリックすることで確認することができます。</p>

![Screenshot 2022-11-07 192100](https://user-images.githubusercontent.com/88228805/200286530-28b405b1-44e3-4a95-98e9-8e27e4c0039d.jpg)

![apikey](https://user-images.githubusercontent.com/88228805/200270237-ad6da86a-0660-48cb-b902-2b5b3de25384.jpg)
<p align="center">図1&nbsp;&nbsp;&nbsp;&nbsp;APIキーの書き方</p>

参考文献:
https://www.sbbit.jp/article/cont1/74706
