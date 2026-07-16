def solution(x):
    answer = True
    num = 0
    for ch in str(x):
        num += int(ch)
    if x % num == 0:
        return True
    else:
        return False