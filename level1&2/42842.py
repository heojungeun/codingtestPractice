def solution(brown, red):
    x = brown
    y = red
    answer = []
    b = -(x+4)/2
    c = x+y
    w = (b*(-1)+(b**2-4*c)**0.5)/2
    h = (x+y)/w
    # if w < 0 or h < 0 or not w.is_integer() or not h.is_integer():
    #     w = (b*(-1)-(b**2-4*c)**0.5)/2
    #     h = (x + y) / w
    if w < h:
        tmp = h
        h = w
        w = tmp
    return [int(w), int(h)]

b = 24
r = 24
print(solution(b,r))