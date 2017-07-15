import winsound
from tones import *
from notes import *

def Interpret(numberNotes):
    # 将“简易音谱”转换成“音乐机器码”
    # 音符，音符拍子，拍子延长符
    # 音符拍子可以是-或者=，对应音符下面的单/双下划线
    # 延长符可以是+对应附点，~对应一个横杠
    ASM_Note = []
    for i, e in enumerate(numberNotes):
        if e in note.keys():
            #检测到是音符
            ASM_Note.append([note[e]])
        elif e in duration.keys():
            #检测到是音长
            ASM_Note[-1].append(duration[e])
        elif e in extension.keys():
            #检测到是音长延长符
            ASM_Note[-1][1] += int(ASM_Note[-1][1] * extension[e])
        else:
            #妈的出错了
            print("Current Note:",numberNotes)
            print("Error:",e,"in index",i)
            exit()
    return ASM_Note

def Play(ASM_Notes):
    # 将完整整理好的“音乐机器码”播放出来：
    #   [音符, 音长], [音符， 音长]
    for freq, time in ASM_Notes:
        winsound.Beep(freq, time)

for row in AlwaysWithMe:
    Play(Interpret(row))
