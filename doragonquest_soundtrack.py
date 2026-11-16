#%%
import numpy as np
import IPython

rate = 48000
duration = 1.0
t = np.linspace(0., duration, int(rate*duration))
x = np.sin(2.0*np.pi*440.0*t)
IPython.display.Audio(x, rate=rate, autoplay=True)
# NumPy配列による440Hz（ラの音）を一秒間鳴らす

#%%
rate = 48000
BPM = 120
qn_duration = 60.0/BPM
t = np.linspace(0., qn_duration, int(rate*qn_duration))
x = np.sin(2.0*np.pi*440.0*t)
IPython.display.Audio(x, rate=rate, autoplay=True)

# BPM=120で4分音符を鳴らす(0.5秒)

#%%
freqs = [0] + [440.0 * 2.0**((i-9)/12.0) for i in range(12)]

# 12音と休符を合わせた13音の周波数

#%%
notes = ["R", "C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
dic = {}
for i, s in enumerate(notes):
    dic[s] = i

# ラ(A)を基準とする
# C=ド　D=レ　E=ミ　F=ファ　G=ソ　A=ラ　B=シ

#%%
def play_mml(mml):
    rate = 48000
    BPM = 120
    qn_duration = 60.0/BPM
    t = np.linspace(0.0, qn_duration, int(rate*qn_duration))
    music = np.array([])
    for s in list(mml):
        f = freqs[dic[s]]
        music = np.append(music, np.sin(2.0*np.pi*f*t))
    return IPython.display.Audio(music, rate=rate, autoplay=True)

#%%
mml_twinkle_star = "CCGGAAGRFFEEDDCRGGFFEEDRGGFFEEDRCCGGAAGRFFEEDDCR"
play_mml(mml_twinkle_star)

#%%
import numpy as np
import IPython

# 基本パラメータ
rate = 48000  # サンプリングレート
BPM = 160  # ビートパー分（テンポ）
qn_duration = 60.0 / BPM  # 4分音符の長さ

# 12音と休符を合わせた周波数リスト
freqs = [0] + [440.0 * 2.0**((i-9)/12.0) for i in range(12)]

# 音符名に対応する辞書
notes = ["R", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
dic = {s: i for i, s in enumerate(notes)}

# MML文字列を再生する関数
def play_mml(mml, note_length=4):
    music = np.array([])  # 音を追加していくリスト
    for note in mml:
        if note.isdigit():  # 数字で音符の長さ指定
            note_length = int(note)  # 音符の長さを更新
        else:
            # 休符の場合は無音、音符の場合はその音の周波数で音を生成
            if note == 'R':
                f = 0.0
            else:
                f = freqs[dic[note]]
            
            # 音符の長さに応じた時間生成
            duration = qn_duration * (4.0 / note_length)  # 音符の長さに応じた

#%%
mml_jokyoku = "EEFGGFEDCCDEEDDEEFGGFEDCCDEDCCDDECDEFECDEFEDCDG"
play_mml(mml_jokyoku)

#%%
#  とりあえず音を鳴らしてみる
import numpy as np
import IPython.display 

BIT_RATE = 44100
concert_pitch = 440

A3 = concert_pitch # ピアノでいう、いわゆる「ラ」の音

duration = 3
sample_A3 = np.sin(A3 * 2 * np.pi * np.linspace(0, duration, duration * BIT_RATE))
IPython.display.Audio(sample_A3, rate=BIT_RATE)

#%%
ratios = [2 ** (i / 12) for i in range(0, 13)]
tone_names = ['A3', 'As3', 'B3', 'C4', 'Cs4', 'D4', 'Ds4', 'E4', 'F4', 'Fs4', 'G4', 'Gs4','A4' ]

TONE_DICT = {}

# A3からA4のクロマチックスケール
for ratio, tone_name in zip(ratios, tone_names):
    duration = 1
    frequency = ratio * A3
    tmp_sound = np.sin(frequency * 2 * np.pi * np.linspace(0, duration, duration * BIT_RATE))
    audio=IPython.display.Audio(tmp_sound, rate=BIT_RATE)

    # あとで使えるように辞書に周波数を入れとく
    TONE_DICT[tone_name] = frequency
    # Jupyter上に表示
    print(f'tone_name:{tone_name}, frequency: {frequency}')
    IPython.display.display(audio)

#%%
# 1オクターブ上、1オクターブ下、2 オクターブ下も作る

# さきほどの1オクターブ分の周波数を作る処理を関数化
def generate_octave(start, tone_names):
    dict_to_return = {}
    for ratio, tone_name in zip(ratios, tone_names):
        frequency = ratio * start
        dict_to_return[tone_name] = frequency
    return dict_to_return

# A2からA3のクロマチックスケール
tone_names_a2_a3 = [ 'A2', 'As2', 'B2', 'C3', 'Cs3', 'D3', 'Ds3', 'E3', 'F3', 'Fs3', 'G3', 'Gs3', 'A3']
a2_a3 = generate_octave(TONE_DICT['A3'] / 2, tone_names_a2_a3)  # 基準音(440Hz)の半分の周波数 = 1オクターブ下の音から始める
TONE_DICT.update(a2_a3)

# A1からA2のクロマチックスケール
tone_names_a1_a2 = [ 'A1', 'As1', 'B1','C2', 'Cs2', 'D2', 'Ds2', 'E2', 'F2', 'Fs2', 'G2', 'Gs2', 'A2']
a1_a2 = generate_octave(TONE_DICT['A3'] / 4, tone_names_a1_a2)  # 基準音(440Hz)の1/4周波数 = 2オクターブ下の音から始める
TONE_DICT.update(a1_a2)

# A4からA5のクロマチックスケール
tone_names_a4_a5 = [ 'A4', 'As4', 'B4','C5', 'Cs5', 'D5', 'Ds5', 'E5', 'F5', 'Fs5', 'G5', 'Gs5', 'A5']
a4_a5 = generate_octave(TONE_DICT['A3'] * 2, tone_names_a4_a5)  # 基準音(440Hz)の4倍の周波数 = 2オクターブ上の音から始める
TONE_DICT.update(a4_a5)

#%%
# 音価(音の長さ)をつくる

QUATER = 1/2
EIGHTH =  QUATER / 2
SIXTEENTH =  EIGHTH / 2


# 周波数と音価からsin波として音を作る関数
def generate_note(frequency, note_value):
    one_sec_note = np.sin(TONE_DICT[frequency] * 2 * np.pi * np.linspace(0, 2, 2 * BIT_RATE))
    return one_sec_note[0:int(len(one_sec_note) * note_value)]

#%%
# 配列を結合する = 音を楽譜で横に並べる = メロディ

c3v4 = generate_note('C3', QUATER)
d3v4 = generate_note('D3', QUATER)
e3v4 = generate_note('E3', QUATER)
f3v4 = generate_note('F3', QUATER)

frog = np.hstack((c3v4, d3v4, e3v4, f3v4, e3v4, d3v4, c3v4))
IPython.display.Audio(frog, rate=BIT_RATE)

#%%
# 配列の和 = 音を楽譜で縦に並べる = ハーモニー

c3v2 = generate_note('C3', QUATER * 2)
e3v2 = generate_note('E3', QUATER * 2)
g3v2 = generate_note('G3',QUATER * 2)

c_triad_chord = np.vstack((c3v2, e3v2, g3v2))
IPython.display.Audio(c_triad_chord, rate=BIT_RATE)


#%%
# ドラゴンクエスト~序曲~すぎやまこういち

melody_notes = [
    ('G3', SIXTEENTH), ('G3', SIXTEENTH), ('C4',EIGHTH), ('D4', EIGHTH),
    ('E4', EIGHTH), ('F4', EIGHTH), ('G4',EIGHTH), ('C5', QUATER),

    ('B4', EIGHTH), ('A4', SIXTEENTH), ('A4', EIGHTH),('G4', EIGHTH), 
    ('Fs4', SIXTEENTH), ('Fs4', SIXTEENTH),('A4', SIXTEENTH), ('G4', EIGHTH), ('E4', QUATER), 
    
    ('E4', SIXTEENTH), ('E4',SIXTEENTH), ('E4', EIGHTH + SIXTEENTH),('E4', EIGHTH + SIXTEENTH),
    ('Fs4', EIGHTH), ('G4', EIGHTH), ('A4', QUATER + SIXTEENTH),

    ('A4', SIXTEENTH), ('B4', SIXTEENTH), ('C5', SIXTEENTH), ('D5', QUATER),
    ('A4', SIXTEENTH), ('A4', SIXTEENTH), ('C5',SIXTEENTH), ('C5', EIGHTH),
    ('B4', EIGHTH), ('A4', EIGHTH), ('G4', EIGHTH), 
    
    ('E4', QUATER + SIXTEENTH), ('F4', SIXTEENTH),
    ('E4', SIXTEENTH), ('D4', SIXTEENTH), ('C4', QUATER), ('A3', EIGHTH),

    ('C4', EIGHTH), ('D4', QUATER + SIXTEENTH), ('E4', SIXTEENTH),('D4', SIXTEENTH), 
    ('C4', SIXTEENTH), ('C4', QUATER), ('B3', EIGHTH), 

    ('G3', EIGHTH), ('G4', QUATER + SIXTEENTH), ('E4', SIXTEENTH), ('F4', SIXTEENTH),
    ('G4', SIXTEENTH), ('A4', QUATER + SIXTEENTH),
    ('A3', SIXTEENTH), ('B3', SIXTEENTH), ('C4', SIXTEENTH), ('F4', QUATER), ('E4', QUATER), ('C4', QUATER + SIXTEENTH),

    ('G3', QUATER), ('G4', SIXTEENTH), ('C4', SIXTEENTH), ('D4', SIXTEENTH), ('E4', SIXTEENTH),
    ('F4', SIXTEENTH), ('E4', SIXTEENTH), ('F4', SIXTEENTH),('G4', SIXTEENTH),('A4', QUATER + EIGHTH),

    ('A3', EIGHTH + SIXTEENTH), ('B3', EIGHTH + SIXTEENTH), ('C4', EIGHTH + SIXTEENTH), ('F4', QUATER + EIGHTH), ('E4', QUATER), ('E4', QUATER), ('C4', QUATER + QUATER)
]

melody_wave = np.hstack([generate_note(tone, value) for tone, value in melody_notes])
melody_audio = IPython.display.Audio(melody_wave, rate=BIT_RATE)
IPython.display.display(melody_audio)

#backing_notes = [
#    ('G4', SIXTEENTH), ('G4', SIXTEENTH), ('C4',EIGHTH), ('B3', EIGHTH), ('A3', EIGHTH), ('G3',EIGHTH),
#    ('E3', QUATER), ('F3', QUATER),
    
#    ('C3', QUATER), ('C3', QUATER), ('C3', EIGHTH), ('E3', EIGHTH), ('G3', QUATER),

#    ('Ds3', EIGHTH), ('D3', EIGHTH), ('C3',EIGHTH), ('B2', EIGHTH), ('A2',EIGHTH), ('C3', EIGHTH), ('E3', QUATER),

#    ('Fs3', EIGHTH), ('A3', EIGHTH), ('D4',EIGHTH), ('D3', EIGHTH), ('G3', EIGHTH), ('D3',EIGHTH), ('G3', QUATER),

#    ('E3', EIGHTH), ('Gs3', EIGHTH), ('B3',EIGHTH), ('E3', EIGHTH), ('A3', EIGHTH), ('B3',EIGHTH), ('C4', EIGHTH), ('A3', EIGHTH),

#    ('Fs3', EIGHTH), ('A3', EIGHTH), ('D4', EIGHTH), ('D3', EIGHTH), ('G3', EIGHTH), ('D3',EIGHTH), ('G3', QUATER),

#    ('E3', EIGHTH), ('Cs3', EIGHTH), ('A2',EIGHTH), ('A2', EIGHTH), ('D3', EIGHTH), ('E3',EIGHTH), ('F3', EIGHTH), ('D3', EIGHTH),

#    ('G3', QUATER), ('G3', QUATER), ('A3', EIGHTH), ('G2', EIGHTH), ('A3', EIGHTH),

#    ('G3', QUATER), ('A2', QUATER), ('D3', EIGHTH), ('C3', EIGHTH), ('B2', QUATER),

#    ('F3', EIGHTH + SIXTEENTH), ('F3', EIGHTH + SIXTEENTH), ('E3', EIGHTH + SIXTEENTH), 
#    ('D3', EIGHTH), ('F3', EIGHTH), ('A3', EIGHTH), ('C4', EIGHTH),
#    ('G3', QUATER), ('G3', QUATER), ('C4', QUATER + QUATER)
#]

#backing_wave = np.hstack([generate_note(tone, value) for tone, value in backing_notes])
#backing_audio = IPython.display.Audio(backing_wave, rate=BIT_RATE)
#IPython.display.display(backing_audio)
#doragonquest_wave = np.vstack((melody_wave, backing_wave)) # メロディとバッキングを合わせる、音の長さが同じでないとエラー
#IPython.display.Audio(doragonquest_wave, rate=BIT_RATE)