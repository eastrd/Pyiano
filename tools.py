from main import *
from notes import *


total = []
for song in [AlwaysWithMe, CastleInTheSky]:
    for row in song:
        total.extend(Interpret(row))



unique_note = [list(x) for x in set(tuple(x) for x in total)]

def song2note(song):
    # 将音符+时长 转换为 ID化
    totalsong = []
    for row in song:
        totalsong.extend(Interpret(row))
    for i, e in enumerate(totalsong):
        if e in unique_note:
            totalsong[i] = unique_note.index(e)
    return totalsong

def note2song(note):
    # 将ID化的代号 转换回 音符+时长
    song = []
    for ele in note:
        try:
            song.append(unique_note[ele])
        except:
            print("list index out of range, ignored...")
            pass
    return song

if __name__=="__main__":
    Play(note2song())
    #print(len(unique_note))
