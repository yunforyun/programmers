def solution(sizes):
    list = [sorted(l, reverse=True) for l in sizes]
    w = max(card[0] for card in list)
    h = max(card[1] for card in list)
              
    return w*h