def solution(nums):
    answer = 0
    combineMaxNum = int(len(set(nums)))
    selectNum = int(len(nums)/2)

    if combineMaxNum >= selectNum:
        answer = selectNum
    else:
        answer = combineMaxNum
    
    return answer