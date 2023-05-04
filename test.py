from collections import Counter

numbers = [3, 30, 34, 5, 9, 90, 900, 901, 96]



stringNumbers = list(map(str, numbers))
#maxLength = len(max(stringNumbers))

answer = []
while True:
    sliceNumber = 1
    
    sliceList = [int(stringNumbers[i][:sliceNumber]) for i in range(len(stringNumbers))]
    counter = Counter(sliceList)
    maxValue = max(counter.keys())
    maxCounter = counter[max(counter.keys())]

    if maxCounter > 1:
        
        tmpList = [stringNumbers[i] for i in range(len(sliceList)) if sliceList[i] == maxValue]
        
        if len(tmpList) >= 2:
            while True:
                reTempList = [int(tmpList[i][0:sliceNumber]) if len(tmpList[i]) == 1 or len(tmpList[i]) < len(max(tmpList)) else int(tmpList[i][sliceNumber:sliceNumber+1]) for i in range(len(tmpList))]
                if len(set(reTempList)) != 1:
                    answer.append(tmpList[reTempList.index(max(reTempList))])
                    del stringNumbers[stringNumbers.index(tmpList[reTempList.index(max(reTempList))])]
                    del tmpList[reTempList.index(max(reTempList))]
                else:
                    sliceNumber += 1
                
                if len(tmpList) == 0:
                    break
        else:
            answer.append(tmpList[0])
            del stringNumbers[stringNumbers.index(tmpList[0])]
            del tmpList[0]
            
    else:
        answer.append(stringNumbers[sliceList.index(maxValue)])
        del stringNumbers[sliceList.index(maxValue)]

    if len(stringNumbers) == 0:
        break
answer

print(''.join(answer))


True - False
False - True