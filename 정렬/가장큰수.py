from collections import Counter

def solution(numbers):
    stringNumbers = list(map(str, numbers))

    answer = []
    while True:
        sliceNumber = 1
        
        sliceList = [int(stringNumbers[i][:sliceNumber]) for i in range(len(stringNumbers))]
        counter = Counter(sliceList)
        maxValue = max(counter.keys())
        maxCounter = counter[max(counter.keys())]

        if maxCounter > 1:
            
            tmpList = [stringNumbers[i] for i in range(len(sliceList)) if sliceList[i] == maxValue]

            for k in range(len(tmpList)):
                reTempList = [int(tmpList[i][0:sliceNumber]) if len(tmpList[i]) == 1 else int(tmpList[i][sliceNumber:sliceNumber+1]) for i in range(len(tmpList))]
                answer.append(tmpList[reTempList.index(max(reTempList))])
                del stringNumbers[stringNumbers.index(tmpList[reTempList.index(max(reTempList))])]
                del tmpList[reTempList.index(max(reTempList))]
        else:
            answer.append(stringNumbers[sliceList.index(maxValue)])
            del stringNumbers[sliceList.index(maxValue)]

        if len(stringNumbers) == 0:
            break

    return ''.join(answer)