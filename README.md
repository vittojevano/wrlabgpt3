# GPT-3, DeepL, and Google STT API for Robot System

DISCLAIMER: This is only for research and personal use only. There won't be any English version of this README.

Main Reference: *[Building Ellee — A GPT-3 and Computer Vision-Powered Talking Robotic Teddy Bear With Human-Level Conversation Intelligence](https://towardsdatascience.com/building-ellee-a-gpt-3-and-computer-vision-powered-talking-robotic-teddy-bear-with-human-level-db7d08259583)*

@2022, Vitto Jevano Christiant
***


## 1. OpenAI GPT-3 API
#### 1.1 GPT-3とは
<p> &nbsp;&nbsp;&nbsp;&nbsp;GPT-3は「Generative Pre-trained Transformer - 3」の略で、OpenAIが開発した事前学習済み（Pre-trained）の文章生成型（Generative）の自然言語処理向けの深層学習モデル「Transformer」、その3番目のモデルを指します。つまり、GPTはTransformerという学習モデルをベースにして、しっかりと事前学習を行い文章生成を行うようにカスタマイズされたAI（言語モデル）ということになります。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;GPT-3は基本的にすべての文章はそれぞれの関係性の一部として理解されます。単語や文章の意味、知識の扱い方については考えておらず、単純に「今日はいい天気ですね」と関係性の深い文章を探し、その次に並べるといった仕組みで運用されます。シンプルですが、シンプルであるがゆえに複雑で膨大なデータであっても扱えますし、応用も簡単です。</p>

<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200279485-a8e993c1-4de1-4e86-b75b-78d5ee4fca31.jpg" alt="gpt3ex">
</div>
<p align="center">図1&nbsp;&nbsp;&nbsp;&nbsp;GPT-3の自然言語処理「Word to Vector」（言葉をベクトル化する）</p>

#### 1.2 GPT-3の使い方

1. OpenAIのURLを開く: https://openai.com/api/
2. 「Sign Up」をクリックし、アカウントを作成する。電話番号やクレジットカードの情報の登録が必要なのでご注意ください。
3. APIキーを設定する。
<p> &nbsp;&nbsp;&nbsp;&nbsp;APIキーはログインした後に右上の「Personal」から「View API Keys」をクリックすることで確認することができます。</p>

<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200286530-28b405b1-44e3-4a95-98e9-8e27e4c0039d.jpg" alt="Screenshot 2022-11-07 192100">
</div>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200302555-02e8ad5a-f474-4d7e-9c7d-00e6ee492bf8.jpg" alt="gptapikey">
</div>
<p align="center">図2&nbsp;&nbsp;&nbsp;&nbsp;View API Keys</p>

4. APIキーをコピーし、apikeyのフォルダを開き、api_secrets.txt の中に直接貼り付ける。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200270237-ad6da86a-0660-48cb-b902-2b5b3de25384.jpg" alt="apikey">
</div>
<p align="center">図3&nbsp;&nbsp;&nbsp;&nbsp;APIキーの書き方</p>

参考文献: <br>
*[ビジネス+IT](https://www.sbbit.jp/article/cont1/74706)* (参照 2022-11-7) <br>
*[楽しみながら理解するAI・機械学習入門](https://data-analytics.fun/2021/12/01/gpt-3-api/)* (参照 2022-11-7)

## 2. DeepL翻訳 API
#### 2.1 DeepL翻訳とは
<p> &nbsp;&nbsp;&nbsp;&nbsp;DeepL翻訳はドイツで言語向けの人工知能システムを開発しているDeepL社が提供している機械翻訳サービスです。DeepL翻訳の前身は、利用者数が十億人以上を誇る世界初の翻訳文の検索エンジンを搭載したLingueeです。DeepL翻訳は2017年夏にインターネット上で無料公開され、2020年3月19日より日本語での利用が可能になりました。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;DeepL翻訳は、深層学習（Deep Learning：ディープラーニング）を利用して翻訳を行っています。
詳しい手法については公表されていませんが、Google翻訳がリカレントニューラルネットワーク（RNN）という深層学習を利用しているのに対し、DeepL翻訳はより複雑な処理が可能な、畳み込みニューラルネットワーク（CNN）と呼ばれる深層学習を用いているのが特徴です。この技術の違いによってDeepL翻訳はGoogle翻訳よりも細かなニュアンスを読み取り、自然で高精度な翻訳が可能となっています。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;DeepL翻訳もプログラムとして使用することができます。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200294420-3526bbb7-1e93-4231-9d44-e35b5247be65.jpg" alt="deepl">
</div>
<p align="center">図4&nbsp;&nbsp;&nbsp;&nbsp;DeepL 翻訳サービス</p>

#### 2.2 DeepL翻訳の使い方

1. DeepL翻訳 APIのURLを開く: https://www.deepl.com/pro-api?cta=header-pro-api
2. 「無料で登録する」をクリックし、無料版のアカウントを作る。クレジットカードの情報の登録が必要なのでご注意ください。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200298208-7cf1982c-1322-4d23-907b-b01b74431686.jpg" alt="deeplapi">
</div>
<p align="center">図5&nbsp;&nbsp;&nbsp;&nbsp;無料で登録する</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;ログインができたらDeepLのアカウントのプラン場面で無料版の「DeepL API Free」に申し込んでいることが確認できます。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200300506-fc9fdadf-6a24-4ed4-9ee7-132b17ff6e98.jpg" alt="deeplfree">
</div>
<p align="center">図6&nbsp;&nbsp;&nbsp;&nbsp;DeepL API Freeの確認</p>

3. アカウント場面の下にDeepL APIで使用する認証キーの確認ができます。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200301412-8fe50786-4767-4ba0-af46-4ae4b831afd6.jpg" alt="deeplapikey">
</div>
<p align="center">図7&nbsp;&nbsp;&nbsp;&nbsp;DeeplのAPIキー</p>
4. APIキーをコピーし、apikeyのフォルダを開き、apideepl.txt の中に直接貼り付ける。

参考文献: <br>
*[Teachme Biz](https://biz.teachme.jp/blog/deepl_translation/)* (参照 2022-11-7)<br>
*[チグサウェブ](https://chigusa-web.com/blog/deepl-api/)* (参照 2022-11-7)

## 3. Google Cloud Speech-to-Text API
#### 3.1 Google Cloudとは

<p> Google Cloud Speech-to-Text APIは音声データから文字起こしをするAPIです。この音声データは音声ファイル(.wavや.flacなど)や、マイクから入力されるストリーム形式まで幅広く対応しています。サービス自体は数年前からありましたが、最近になりストリーミング音源のテキスト起こしが時間無制限でできるようになったみたいなので試してみました。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200306239-cbaa8a3e-4fe1-4939-b40f-c574976acf16.jpg" alt="googlestt">
</div>
<p align="center">図8&nbsp;&nbsp;&nbsp;&nbsp;Google Cloud Speech-to-Text</p>

参考文献: <br>
*[Optim Tech Blog](https://tech-blog.optim.co.jp/entry/2020/02/21/163000#Google-Cloud-Speech-to-Text-API-%E3%81%A8%E3%81%AF)* (参照 2022-11-7)

