def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key=lambda x: x*4, reverse=True)
    result = ''.join(answer)

    if result[0] == '0':
        return '0'
    return result