def solution(answers):
    person1, person2, person3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    persons = [person1, person2, person3]

    answer = []
    for person in persons:
        cycleNum, remainNum = len(answers) // len(person), len(answers) % len(person)
        method = (person * cycleNum) + person[:remainNum]
        
        count = 0
        for idx in range(len(answers)):
            correctNumber = answers[idx]
            
            if correctNumber == method[idx]:
                count+=1
        
        answer.append(count)
        
        maxPerson = [i+1 for i in range(len(answer)) if answer[i] == max(answer)]
        
    return maxPerson