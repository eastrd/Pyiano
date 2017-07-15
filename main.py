import winsound


Beat = 600
_Beat = Beat // 2
__Beat = Beat // 4
Two_Beats = Beat * 3 // 2

duration = {
    "." : Beat,
    "-" : _Beat,
    "=" : __Beat,
    "~" : Two_Beats
}

note = {
    " " : 37,
    "q" : 131,
    "w" : 147,
    "e" : 165,
    "r" : 174,
    "t" : 196,
    "y" : 220,
    "u" : 247,
    "1" : 262,
    "2" : 294,
    "3" : 330,
    "4" : 349,
    "5" : 392,
    "6" : 440,
    "7" : 494,
    "z" : 523,
    "x" : 587,
    "c" : 659,
    "v" : 698,
    "b" : 784,
    "n" : 880,
    "m" : 988
}

def Play_key(freq, duration):
    winsound.Beep(freq, duration)

def FilterChunk(numberNotes):
    # Convert shorthanded number notes into machine readable format
    Note = []
    for i, e in enumerate(numberNotes):
        if e in note.keys():
            Note.append(e)
        elif e == "+":
            #附点音符，之前的音长 * 1.5
            Note[-1] += "+"
        else:
            #音长
            Note[-1] += e
    for i in range(len(Note)):
        if len(Note[i]) == 1:
            Note[i] = Note[i] + "."
    print(Note)

def Play_Chunk(ASM_Notes):
    for freq, time in ASM_Notes:
        #print(freq, time)
        Play_key(note[freq], duration[time])

def Play(Notes):
    # Wrapper function
    Play_Chunk(FilterChunk(Notes))

#回梦游仙
a = "c-x-cc-6-x z=7=6-7=6-5-33-5-z3-5-76-5-6 c-xc-x-cc-6-x z=7=6- -6=6-5-33-5-z3-5-x- -c=x-5-6  7  7  7  "

#天空之城
b = "6-7-z 7-zc7  36 5-6z5  4-3-4 3-4z3  -z-z-z-7 4-477  6-7-z 7-zc7  3-3-6 5-6z5  34z-7zxc-z- z-7-6756  z-x-c x-cbx  5-5-z 7-zcc   6-7-z7-z-xz 5-5 vcxzccccc  cn b cx-z- "

#风之甬道
c = "e-t-yy-u-te-t-yy-2-uu-2-3-3-3-5-4-3-2-1-uy-e-ue-t-yy-u-te-t-yy-2-uu-2-3-3-3-5-4-3-u-e-t-  e-t-yy-u-5e-t-yy-2-uu-2-3-3-3-5-4-3-2-1-"

#可惜不是你
d = "1=3-2=3=3=5- -5-3=2=2- -1=1   - -5=6-5=6=6=z- -z-5=5=5-3-2-2-2  - -2=3-2=3=3=5- -"

# Always with Me
e = "1-2-3-1-5 3-2521-y-3 1-u uyu1-2-t12-3-44-3-2-1-2 1-2-3-1-5 3-252-2-1-y-yu-1-t tyu1-2-t12-3-44-3-2-1-1~ 3-4-55555-6-5-4-33333-4-3-2-111-u-yuu-1-22-3-2-3-2 3-4-55555-6-5-4-3333-4-3-2-1-u-yy-u-1-2-t12-3-2 2-2-1-1~    "
f = "1-+2-3-+"
#Play(e)
FilterChunk(f)
