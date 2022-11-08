# GPT-3, DeepL, and Google STT API for Robot System

DISCLAIMER: This is only for research and personal use only. There won't be any English version of this README.

Main Reference: *[Building Ellee — A GPT-3 and Computer Vision-Powered Talking Robotic Teddy Bear With Human-Level Conversation Intelligence](https://towardsdatascience.com/building-ellee-a-gpt-3-and-computer-vision-powered-talking-robotic-teddy-bear-with-human-level-db7d08259583)*

@2022, Vitto Jevano Christiant
***

# I. APIの紹介と設定

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
2. 「無料で登録する」をクリックし、無料版のアカウントを作成する。クレジットカードの情報の登録が必要なのでご注意ください。
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
#### 3.1 Google Cloud Speech-to-Text とは

<p> Google Cloud Speech-to-Text APIは音声データから文字起こしをするAPIです。この音声データは音声ファイル(.wavや.flacなど)や、マイクから入力されるストリーム形式まで幅広く対応しています。サービス自体は数年前からありましたが、最近になりストリーミング音源のテキスト起こしが時間無制限でできるようになったみたいなので試してみました。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200306239-cbaa8a3e-4fe1-4939-b40f-c574976acf16.jpg" alt="googlestt">
</div>
<p align="center">図8&nbsp;&nbsp;&nbsp;&nbsp;Google Cloud Speech-to-Text</p>

#### 3.2 Google Cloud Speech-to-Textの使い方
1. Google Cloud ConsoleのURLを開く:https://console.cloud.google.com/
2. 「無料トライアルに登録」をクリックし、Google Cloudアカウントを作成する。クレジットカードの情報の登録が必要なのでご注意ください。

<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200508442-aa83cc9c-2837-4697-a349-16a91b2f9efa.jpg" alt="gcptrial">
</div>
<p align="center">図9&nbsp;&nbsp;&nbsp;&nbsp;無料トライアルに登録</p>

3. ログインができたら、「Google Cloud」の右側にプロジェクトリストを開く。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200508607-2295ac02-e13b-4d1d-b6ae-576d0500b6b6.jpg" alt="gcpproject1">
</div>
<p align="center">図10&nbsp;&nbsp;&nbsp;&nbsp;プロジェクトリストを開く</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;新しいプロジェクトをクリックする。次に、プロジェクト名等を記入し、新しいプロジェクトを作成する。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200508733-75ea7917-68e0-4b3c-8c58-cd66d3ea8ced.jpg" alt="gcpproject2">
  <img src="https://user-images.githubusercontent.com/88228805/200508853-6029d25c-b6f6-4284-9e13-9cc5ad9c2d8c.jpg" alt="gcpproject3">
</div>

<p align="center">図11&nbsp;&nbsp;&nbsp;&nbsp;新しいプロジェクトの作成</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;プロジェクトリストを再び開き、作成したプロジェクトを開く。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200509021-fdd8518f-cf22-4c1c-a355-c9f6991d924d.jpg" alt="gcpproject4">
</div>
<p align="center">図12&nbsp;&nbsp;&nbsp;&nbsp;作成したプロジェクトを開く</p>

4. ナビゲーションメニューを開き、「APIとサービス」の「ライブラリー」を開く。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200509653-44f84a4d-3e4f-4e9d-986a-bf3798888efa.jpg" alt="sttlibrary">
</div>
<p align="center">図13&nbsp;&nbsp;&nbsp;&nbsp;APIのライブラリー</p>

5. 検索場面にSpeech-to-Textを検索し、「Cloud Speech-to-Text API」をクリックする。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200514647-ea371dac-ae9f-485d-91c2-05ebd63f5ff0.jpg" alt="sttapi">
</div>
<p align="center">図14&nbsp;&nbsp;&nbsp;&nbsp;Cloud Speech-to-Text API</p>

6. 「Cloud Speech-to-Text API」の場面に「有効にする」ボタンをクリックする。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200515511-d5887ef2-47ca-42d7-9d7b-50ea71cdd8a8.jpg" alt="enablestt">
</div>
<p align="center">図15&nbsp;&nbsp;&nbsp;&nbsp;「有効にする」ボタンをクリックする</p>

7. 検索場面にCloud Storage APIを検索し、「Cloud Storage API」をクリックし、「有効にする」ボタンをクリックする。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200516526-f593f6de-b438-4e1d-9749-a2ea1b1bd632.jpg" alt="cloudstorageapi">
  <img src="https://user-images.githubusercontent.com/88228805/200517300-c2823744-8244-492d-99fe-2cb89a7500b6.jpg" alt="csapi">
</div>
<p align="center">図16&nbsp;&nbsp;&nbsp;&nbsp;Cloud Storage API</p>

8. 検索場面にCloud Storage JSON APIを検索し、「Google Cloud Storage JSON API」をクリックし、「有効にする」ボタンをクリックする。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200517922-7390da7a-731e-4b3d-a714-aefc6a22e3dd.jpg" alt="csjsonapi1">
  <img src="https://user-images.githubusercontent.com/88228805/200518019-0012e36b-6d37-4890-87fd-4f6e15b57233.jpg" alt="csjsonapi2">
</div>
<p align="center">図17&nbsp;&nbsp;&nbsp;&nbsp;Google Cloud Storage JSON API</p>

9. ナビゲーションメニューを開き、「IAMと管理」の「サービスアカウント」を開く。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200535649-90674470-4d50-404c-9ec3-720f0d9ffd07.jpg" alt="serviceacc">
</div>
<p align="center">図18&nbsp;&nbsp;&nbsp;&nbsp;サービスアカウント</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;「サービスアカウントを作成」のボタンをクリックする。次に、サービスアカウント名を気入し、「作成して続行」ボタンをクリックする。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200535949-d4f5054f-4d4c-4504-a024-b4bde36a9f66.jpg" alt="serviceacc1">
  <img src="https://user-images.githubusercontent.com/88228805/200536038-8f866067-237b-4bb9-b8e0-91bb304931b9.jpg" alt="serviceacc2">
</div>
<p align="center">図19&nbsp;&nbsp;&nbsp;&nbsp;サービスアカウントの作成</p>  

<p>&nbsp;&nbsp;&nbsp;&nbsp;「このサービス アカウントにプロジェクトへのアクセスを許可する」、「ユーザーにこのサービス アカウントへのアクセスを許可」を省略し、「続行」、「完了」ボタンをクリックする。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200536233-e68fc658-85bd-44be-871c-1ff19ee23ab6.jpg" alt="serviceacc3">
</div>
<p align="center">図20&nbsp;&nbsp;&nbsp;&nbsp;サービスアカウントの作成の続き</p>  

10. サービスアカウントで作成したアカウントの右側に三つの点をクリックし、「鍵を管理」をクリックする。
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200537069-6474023e-c138-4cf8-a2d3-7d9d6800b4cb.jpg" alt="sttkey">
</div>
<p align="center">図21&nbsp;&nbsp;&nbsp;&nbsp;「鍵を管理」をクリック</p>  

  
<p>&nbsp;&nbsp;&nbsp;&nbsp;「鍵を追加」をクリックし、「新しい鍵を作成」を選択し、「JSON」で鍵を作成する。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200536980-8e008f50-dfea-4fd5-bf52-b82f8c8dc2d0.jpg" alt="sttkey2">
  <img src="https://user-images.githubusercontent.com/88228805/200537221-0bf77c3e-29f1-4334-805b-dbc8da7807b9.jpg" alt="sttkey3">
</div>
<p align="center">図22&nbsp;&nbsp;&nbsp;&nbsp;新しい鍵を作成する</p>   


<p>&nbsp;&nbsp;&nbsp;&nbsp;作成が完成したらGoogle Cloud APIキーがダウンロードされます。</p>
<div align="center">
  <img src="https://user-images.githubusercontent.com/88228805/200538971-340fa944-8a34-4530-9150-6d736a0a1b2c.jpgg" alt="sttkey4">
</div>
<p align="center">図23&nbsp;&nbsp;&nbsp;&nbsp;Google Cloud APIキー</p>   

11. 作成したGoogle Cloud APIキーを全てコピーし、apikeyのフォルダを開き、Cloud_KEY.jsonの中に貼り付ける。


参考文献: <br>
*[Optim Tech Blog](https://tech-blog.optim.co.jp/entry/2020/02/21/163000#Google-Cloud-Speech-to-Text-API-%E3%81%A8%E3%81%AF)* (参照 2022-11-7)　<br>
*[Youtube チュートリアル](youtube.com/watch?v=lKra6E_tp5U&t=654s)* (参照 2022-11-8)
