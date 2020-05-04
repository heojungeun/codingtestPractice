def solution(m, musicinfos):
    answer = []
    for idx, x in enumerate(musicinfos):
        stime, etime, title, music = x.split(",")
        bhour, bmin = map(int,stime.split(":"))
        ahour, amin = map(int,etime.split(":"))
        if amin-bmin < 0:
            submin = amin-bmin + 60
            ahour -= 1
        else:
            submin = amin - bmin
        submin = (ahour-bhour)*60+submin
        be = ["C#","D#","F#","G#","A#"]
        af = ["c","d","f","g","a"]
        for i in range(5):
            m = m.replace(be[i],af[i])
            music = music.replace(be[i],af[i])
        p, r = divmod(submin,len(music))
        ori = music*p + music[:r]
        if m in ori:
            answer.append((submin,idx,title))
    if len(answer):
        answer.sort(key=lambda x: (-x[0], x[1]))
        return answer[0][2]
    return "(None)"

mstr = "CC#BCC#BCC#BCC#B"
minfo = ["03:00,03:30,FOO,CC#B","04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(mstr,minfo))