import itertools
def solution(numbers):
    result = []

    for i in range(len(numbers)):
        perms = itertools.permutations(numbers, i + 1)
        for p in perms:
            num = int(''.join(p))  # 튜플을 문자열로 만들고 정수로 변환
            result.append(num)

    # print(result)
    decimal = {}
    decimal = set(decimal)
    for num in result:
        for i in range(2, num+1):
            if num % i == 0 and i != num:
                break
            elif num %i == 0 and i == num:
                decimal.add(num)
    return len(decimal)  