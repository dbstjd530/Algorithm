# n: 학생 수 / lost : 도난당한 학생 번호 / reserve : 여벌의 체육복을 가져온 학생 번호 / return : 수업을 들을 수 있는 학생의 최대값
def solution(n, lost, reserve):
    student = [num for num in range(1,n+1)]
    newLost = [i for i in lost if i not in reserve]
    newReserve = [j for j in reserve if j not in lost]

    newStudent = list(map(lambda x: 0 if x in newLost else (2 if x in newReserve else 1),student))

    for person in newLost:
        if person - 1 in newReserve:
            newStudent[person-1] += 1
            newStudent[person-2] -= 1 
            
        elif person + 1 in newReserve:
            newStudent[person-1] += 1
            newStudent[person] -= 1

    answer = len(list(filter(lambda x: x > 0, newStudent)))
    return answer