def solution(brown, red):
    b = (brown/2)-2
    y = int((b + (b ** 2 - 4 * red) ** 0.5) / 2)
    if y<0:
        y = int((b - (b ** 2 - 4 * red) ** 0.5) / 2)
    yw = red // y
    if yw < y:
        return [y + 2, yw + 2]
    return [yw + 2, y + 2]

print(solution(10,2))