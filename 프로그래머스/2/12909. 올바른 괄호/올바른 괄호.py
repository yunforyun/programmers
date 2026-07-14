def solution(s):
    answer = True
    cnt = 0
    for str in s:
        if str == '(':
            cnt += 1
        elif str == ')':
            cnt -= 1
        
        if cnt < 0:
            return False
    if cnt > 0:
        return False
    return True