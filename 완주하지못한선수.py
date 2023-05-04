def solution(participant, completion):
    for name in range(len(completion)):
       selectName = completion[name]
       
       if selectName in participant:
            participant.remove(selectName)

    answer = participant.pop()
    return answer