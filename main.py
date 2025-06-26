# Copyright Anis AYARI (Defend Intelligence)
# N'oubliez pas de citer le projet d'origine ! Merci !

import sounddevice as sd
import openai
import pyaudio
import wave
from dotenv import load_dotenv, find_dotenv
from elevenlabs import generate, stream, set_api_key
from pydub import AudioSegment
from pydub.playback import play
import pvporcupine
from pvrecorder import PvRecorder
import os
import random
import signal
import time

load_dotenv(find_dotenv())

porcupine = pvporcupine.create(
    access_key=os.getenv('ACCES_KEY_PORCUPINE'),
    keyword_paths=[os.getenv('KEYWORD_PATH_PORCUPINE')],
    model_path=os.getenv('MODEL_PATH_PROCUPINE')
)
set_api_key(os.getenv('ELEVENLAB_API_KEY'))
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORG')
sd.query_devices()

def record_audio(filename, duration=5):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("🎙️ Recording...")
    frames = [stream.read(CHUNK) for _ in range(0, int(RATE / CHUNK * duration))]
    print("✅ Recording finished")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def transcribe_audio(filename):
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]

def get_generate_audio(text):
    audio = generate(
        text=text,
        voice=os.getenv("ELEVENLAB_VOICE_ID"),
        model="eleven_multilingual_v1",
        stream=True
    )
    stream(audio)

def generate_script_gpt(text, messages_prev):
    if not messages_prev:
        messages_prev = [
            {
              "role": "system",
              "content": "Tu es l’IA personnelle de Dofla, streamer et YouTuber français.\n\nTu penses comme lui : franc, tranchant, anti-hypocrisie. Tu balances quand ça pue l'enfumage.\n\nTon ton : mordant, sarcastique, drôle, direct. Parfois absurde, souvent ironique, toujours percutant.\n\nTu réagis comme Dofla : tu cites des mèmes, Twitch, Twitter, tu dézingues les arguments creux avec une punchline, tu respectes ceux qui sont droits.\n\nTu ne fais pas de langue de bois. Tu trolles intelligemment. Tu simplifies quand ça fume trop, tu montres les contradictions.\n\nEt surtout : t’es jamais chiant. 3 phrases max. T’as la vanne facile et la réplique qui claque. Si tu t’ennuies, c’est que t’as mal bossé."
            }

            {"role": "user", "content": text}
        ]
    else:
        messages_prev.append({"role": "user", "content": text})

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        max_tokens=150,
        temperature=1,
        messages=messages_prev
    )

    res = response['choices'][0]['message']['content']
    messages_prev.append({"role": "assistant", "content": res})

    if len(messages_prev) > 10:
        messages_prev = messages_prev[-10:]

    return res, messages_prev

def handle_interaction(messages_prev):
    audio_filename = "recorded_audio.wav"
    record_audio(audio_filename)
    transcription = transcribe_audio(audio_filename)
    print(f"📝 {transcription}")

    if "merci" in transcription.lower():
        print("🙏 Fin de l'écoute continue")
        return messages_prev, True

    res, messages_prev = generate_script_gpt(transcription, messages_prev)
    get_generate_audio(res)
    return messages_prev, False

def get_random_mp3_file(folder_path):
    mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    if not mp3_files:
        return None
    return os.path.join(folder_path, random.choice(mp3_files))

def signal_handler(sig, frame):
    print("\nProgramme terminé.")
    recorder.stop()
    exit(0)

if __name__ == "__main__":
    messages_prev = []
    print('🎧 En attente du mot-clé...')
    recorder = PvRecorder(frame_length=porcupine.frame_length)
    recorder.start()
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        pcm = recorder.read()
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("🔊 Mot-clé détecté")
            path = get_random_mp3_file('voix_intro')
            if path:
                play(AudioSegment.from_file(path))

            messages_prev, stop = handle_interaction(messages_prev)

            # 🔁 Mode écoute rapide : 5 sec max, ou "merci"
            start_time = time.time()
            while not stop and time.time() - start_time < 5:
                print("⏱️ Écoute rapide...")
                pcm = recorder.read()
                keyword_index = porcupine.process(pcm)
                if keyword_index == -1:
                    messages_prev, stop = handle_interaction(messages_prev)
                    start_time = time.time()
