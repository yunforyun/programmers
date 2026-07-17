def solution(triangle):
    dp = [triangle[0]]
    
    for i in range(1, len(triangle)):
        row = triangle[i]
        prev = dp[-1]
        new_row = []
        
        for j, val in enumerate(row):
            if j == 0:
                new_row.append(val+prev[0])
            elif j == len(row) - 1:
                new_row.append(val+prev[-1])
            else :
                new_row.append(max(val+prev[j-1], val+prev[j]))
        dp.append(new_row)

    return max(dp[-1])