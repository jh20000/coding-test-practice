def solution(answer):

    s1 = [1, 2, 3, 4, 5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    le = len(answer)
    # 차원수 맞춰주고
    s1 = s1*(le//len(s1)+1)
    s2 = s2*(le//len(s2)+1)
    s3 = s3*(le//len(s3)+1)

    a = [0,0,0]


    for i in range(len(answer)):
        if s1[i] == answer[i]:
            a[0] += 1
        if s2[i] == answer[i]:
            a[1] += 1
        if s3[i] == answer[i]:
            a[2] += 1

    m = max(a)
    ans = []
    for idx in range(3):
        if m == a[idx]:
            ans.append(idx+1)

    return ans