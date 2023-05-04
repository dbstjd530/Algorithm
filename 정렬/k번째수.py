def solution(array, commands):
    
    answer = []
    for command in commands:
        i,j,k = command
        sliceArray = sorted(array[i-1:j])
        answer.append(sliceArray[k-1])
        
    return answer