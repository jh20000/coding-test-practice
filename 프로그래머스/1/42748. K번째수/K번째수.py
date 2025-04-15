def solution(array, commands):
    ans = []

    for c in commands:
        #arr 초기화
        arr = []
        #슬라이싱으로 추출
        arr = array[c[0]-1:(c[1])]
        #정렬
        arr.sort()
        
        ans.append(arr[c[2]-1])

    return ans    
