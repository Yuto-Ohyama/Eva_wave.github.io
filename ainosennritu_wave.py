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

# 休符
tone_names_R = ['R']
R = generate_octave(TONE_DICT['A3'] * 0, tone_names_R)  # 基準音(440Hz)の0倍の周波数 = 休符
TONE_DICT.update(R)

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
# 愛の旋律~ドラゴンクエストⅤ~

melody_notes = [

    ('C3', EIGHTH), ('D3', SIXTEENTH), ('E3', SIXTEENTH), 
    ('A3', SIXTEENTH), ('Fs3', QUATER + QUATER), 
    # ドレミラsファ
    ('E3', EIGHTH), ('Fs3', SIXTEENTH), ('G3', SIXTEENTH), 
    ('B3', SIXTEENTH), ('Fs3', QUATER + QUATER), 
    # ミsファソシsファ
    ('E3', EIGHTH), ('Fs3', SIXTEENTH), ('G3', SIXTEENTH), 
    ('B3', SIXTEENTH), ('As3', QUATER + QUATER), 
    # ミsファソシsシ
    ('Gs3', EIGHTH), ('As3', SIXTEENTH), ('B3', SIXTEENTH), 
    ('Ds4', SIXTEENTH), ('As3', QUATER + QUATER), 
    # sラsシシsミsシ

    ('Gs3', EIGHTH), ('As3', SIXTEENTH), ('B3', SIXTEENTH), 
    ('Ds4', SIXTEENTH), ('F4', SIXTEENTH), ('C4', SIXTEENTH), 
    ('D4', SIXTEENTH), ('A3', QUATER + SIXTEENTH),
    # sラsシシsミファドレラ
    ('As3', SIXTEENTH + SIXTEENTH/2), ('C4', SIXTEENTH + SIXTEENTH/2), ('D4', SIXTEENTH + SIXTEENTH/2), 
    ('F4', SIXTEENTH), ('C4', SIXTEENTH), 
    ('D4', SIXTEENTH), ('A3', QUATER + SIXTEENTH),
    # sシドレファドレラ
    ('As3', SIXTEENTH + SIXTEENTH/2), ('C4', SIXTEENTH + SIXTEENTH/2), ('D4', SIXTEENTH + SIXTEENTH/2), 
    ('G4', SIXTEENTH), ('D4', SIXTEENTH), 
    ('C4', SIXTEENTH), ('As3', QUATER),
    # sシドレソレドsシ
    ('A3', SIXTEENTH), ('G3', SIXTEENTH), ('Ds3', SIXTEENTH), 
    ('C3', SIXTEENTH), ('D3', SIXTEENTH), 
    ('Ds3', SIXTEENTH), ('D3', QUATER + QUATER),
    # ラソsミドレsミレ


    ('C4', EIGHTH), ('D4', SIXTEENTH), ('E4', SIXTEENTH), 
    ('A4', SIXTEENTH), ('Fs4', QUATER + QUATER), 
    # ドレミラsファ
    ('E4', EIGHTH), ('Fs4', SIXTEENTH), ('G4', SIXTEENTH), 
    ('B4', SIXTEENTH), ('Fs4', QUATER + QUATER), 
    # ミsファソシsファ
    ('E4', EIGHTH), ('Fs4', SIXTEENTH), ('G4', SIXTEENTH), 
    ('B4', SIXTEENTH), ('As4', QUATER + QUATER), 
    # ミsファソシsシ
    ('Gs4', EIGHTH), ('As4', SIXTEENTH), ('B4', SIXTEENTH), 
    ('Ds5', SIXTEENTH), ('As4', QUATER + QUATER), 
    # sラsシシsミsシ

    ('Gs4', EIGHTH), ('As4', SIXTEENTH), ('B4', SIXTEENTH), 
    ('Ds5', SIXTEENTH), ('F5', SIXTEENTH), ('C5', SIXTEENTH), 
    ('D5', SIXTEENTH), ('A4', QUATER + SIXTEENTH),
    # sラsシシsミファドレラ
    ('As4', SIXTEENTH + SIXTEENTH/2), ('C5', SIXTEENTH + SIXTEENTH/2), ('D5', SIXTEENTH + SIXTEENTH/2), 
    ('F5', SIXTEENTH), ('C5', SIXTEENTH), 
    ('D5', SIXTEENTH), ('A4', QUATER + SIXTEENTH),
    # sシドレファドレラ
    ('As4', SIXTEENTH + SIXTEENTH/2), ('C5', SIXTEENTH + SIXTEENTH/2), ('D5', SIXTEENTH + SIXTEENTH/2), 
    ('G5', SIXTEENTH), ('D5', SIXTEENTH), 
    ('C5', SIXTEENTH), ('As4', QUATER),
    # sシドレソレドsシ
    ('A4', SIXTEENTH), ('G4', SIXTEENTH), ('Ds4', SIXTEENTH), 
    ('C4', SIXTEENTH), ('D4', SIXTEENTH), 
    ('Ds4', SIXTEENTH), ('D4', QUATER + EIGHTH), ('D4', EIGHTH + SIXTEENTH),
    # ラソsミドレsミレ

    ('D4', EIGHTH + SIXTEENTH), ('Ds4', QUATER + SIXTEENTH), ('Ds4', SIXTEENTH), 
    ('F4', SIXTEENTH), ('G4', SIXTEENTH), ('A4', SIXTEENTH), 
    ('G4', SIXTEENTH), ('F4', SIXTEENTH), ('D5', QUATER),
    # レsミsミファソラソファレ
    ('A4', SIXTEENTH), ('G4', SIXTEENTH), ('A4', QUATER), 
    ('G4', SIXTEENTH), ('F4', SIXTEENTH), ('Ds4', SIXTEENTH), 
    ('F4', EIGHTH), ('F4', SIXTEENTH), ('Ds4', SIXTEENTH), 
    # ラソラソファsミファファsミ

    ('D4', SIXTEENTH), ('E4', SIXTEENTH), ('Fs4', SIXTEENTH), 
    ('G4', SIXTEENTH), ('A4', SIXTEENTH), ('As4', SIXTEENTH), 
    ('C5', QUATER), ('G4', SIXTEENTH), ('A4', SIXTEENTH), 
    ('G4', SIXTEENTH), ('A4', EIGHTH + SIXTEENTH), 
    ('C4', EIGHTH), ('F4', SIXTEENTH), 
    # レミsファソラsシドソラソラドファ

    ('D4', SIXTEENTH), ('F4', SIXTEENTH), ('A4', SIXTEENTH), 
    ('C5', SIXTEENTH), ('A4', SIXTEENTH), ('F4', SIXTEENTH), 
    ('D4', QUATER), ('As3', SIXTEENTH), ('C4', SIXTEENTH), 
    # レファラドラファレsシド

    ('D4', SIXTEENTH), ('F4', SIXTEENTH), ('A4', SIXTEENTH), 
    ('C5', SIXTEENTH), ('A4', SIXTEENTH), ('F4', SIXTEENTH), 
    ('D4', QUATER),  
    # レファラドラファレ

    ('As3', SIXTEENTH), ('C4', SIXTEENTH), ('D4', SIXTEENTH), 
    ('Ds4', SIXTEENTH), ('F4', SIXTEENTH), ('G4', SIXTEENTH), 
    ('A4', SIXTEENTH), ('As4', SIXTEENTH), ('C5', SIXTEENTH), 
    ('As4', SIXTEENTH), ('A4', SIXTEENTH), 
    ('G4', SIXTEENTH), ('A4', SIXTEENTH), 
    ('As4', SIXTEENTH), ('As4', SIXTEENTH), 
    # sシドレsミファソラsシドsシラソラsシsシ

    ('D2', SIXTEENTH), ('Fs2', SIXTEENTH), ('As2', SIXTEENTH), 
    ('C3', SIXTEENTH), 
    ('D3', SIXTEENTH), ('Fs3', SIXTEENTH), ('As3', SIXTEENTH), 
    ('C4', SIXTEENTH),  
    ('D4', SIXTEENTH), ('Fs4', SIXTEENTH), ('As4', SIXTEENTH), 
    # レsファsシドレsファsシドレsファsシ
    
    ('A4', SIXTEENTH), ('Fs4', SIXTEENTH), ('D4', SIXTEENTH), 
    ('C4', SIXTEENTH), 
    ('A3', SIXTEENTH), ('Fs3', SIXTEENTH), ('D3', SIXTEENTH), 
    # ラsファレドラsファレ

    ('C3', EIGHTH), ('D3', SIXTEENTH), ('E3', SIXTEENTH), 
    ('A3', SIXTEENTH), ('Fs3', QUATER + QUATER), 
    # ドレミラsファ
    ('E3', EIGHTH), ('Fs3', SIXTEENTH), ('G3', SIXTEENTH), 
    ('B3', SIXTEENTH), ('Fs3', EIGHTH), 
    # ミsファソシsファ

    ('G2', EIGHTH), ('E3', EIGHTH), ('B3', EIGHTH), 
    ('D4', EIGHTH), ('Fs4', EIGHTH), ('A4', EIGHTH), 
    # ソミシレsファラ

]

melody_wave = np.hstack([generate_note(tone, value) for tone, value in melody_notes])
kekkonV_1_audio = IPython.display.Audio(melody_wave, rate=BIT_RATE)
IPython.display.display(kekkonV_1_audio)

# %%