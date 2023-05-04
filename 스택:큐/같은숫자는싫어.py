def solution(arr):
   
    answer = []
    compareNumber = -1
    for num in arr:
        if compareNumber != num:
            answer.append(num)
            compareNumber = num
        
    return answer