
from pytube import YouTube
import speech_recognition as sr

import os
import subprocess


def download_audio(url, output_path):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path)
    return audio_stream.default_filename


def convert_to_wav(audio_file, output_path):
    file_name, _ = os.path.splitext(os.path.basename(audio_file))
    wav_file = os.path.join(output_path, f"{file_name}.wav")
    subprocess.run(['ffmpeg', '-i', audio_file, wav_file])
    return wav_file


def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='en') # Set default language to English .. YOU CAN CHANGE IT AS U WANT
    return text


def save_text(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == "__main__":
    video_url = ''  # add your yt link here btw ''
    output_path = 'OUTPUT_FOLDER_PATH'
    output_file = 'OUTPUT_TEXT_FILE_PATH'

    audio_file = download_audio(video_url, output_path)
    wav_file = convert_to_wav(os.path.join(output_path, audio_file), output_path)
    text = audio_to_text(wav_file)
    save_text(text, output_file)

