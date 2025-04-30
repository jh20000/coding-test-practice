
def solution(sizes):


    #가로세로연구소
    for i in sizes:
        i.sort()

    #max값 뽑기

    e1 = []
    e2 = []
    for i in range(len(sizes)):
        e1.append(sizes[i][0])
        e2.append(sizes[i][1])


    return (max(e1) * max(e2))
