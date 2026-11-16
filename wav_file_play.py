#%%
import wave
import pyaudio

def play_wav(filename):
    wav_file = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                    channels=wav_file.getnchannels(),
                    rate=wav_file.getframerate(),
                    output=True)

    data = wav_file.readframes(1024)
    while data:
        stream.write(data)
        data = wav_file.readframes(1024)

    stream.stop_stream()
    stream.close()
    p.terminate()

play_wav('v2_melody.wav')
#%%
# 効果音ラボ　音声フリー素材
from playsound import playsound

playsound("学校のチャイム.mp3")

#%%
#coding:utf-8
import pygame.mixer
import time

def sound():
    pygame.mixer.init() #初期化

    pygame.mixer.music.load("学校のチャイム.mp3") #読み込み　wavもmp3も可

    pygame.mixer.music.play(2) #再生

    time.sleep(40) # 再生時間

    pygame.mixer.music.stop() #終了

if __name__ == '__main__':
    sound()
