def solution(answers):
    score = [0,0,0]
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        answer = answers[i]
        if student1[i % len(student1)] == answer:
            score[0] += 1
        if student2[i % len(student2)] == answer:
            score[1] += 1
        if student3[i % len(student3)] == answer :
            score[2] += 1
    best = max(score)
    stu = []
    for i in range(len(score)):
        if score[i] == best:
            stu.append(i+1)
        
    return sorted(stu)