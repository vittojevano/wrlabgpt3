import os
from google.cloud import speech

Cloud_KEY = "C:\Research\Speech\Cloud_KEY.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Cloud_KEY
speech_client = speech.SpeechClient()

# Step 1: 音声データをロードする
media_file_name = "C:\Research\Speech\demo.mp3"

with open(media_file_name, 'rb') as f1:
    byte_data = f1.read()
audio = speech.RecognitionAudio(content=byte_data)

# Step 2: 音声データを読み取る
config = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US',
)

# Step 3: 読み取った音声データを書き写す
response = speech_client.recognize(
    config=config,
    audio=audio,
)

print(response)