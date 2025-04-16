from functools import cmp_to_key

def compare(a, b):
    # a+b와 b+a를 비교해서 더 큰 쪽이 앞으로 오도록
    if a + b > b + a:
        return -1  # a가 먼저
    elif a + b < b + a:
        return 1   # b가 먼저
    else:
        return 0

def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 정렬 (비교 함수를 기반으로)
    numbers.sort(key=cmp_to_key(compare))
    
    # 0만 여러 개 있을 경우
    if numbers[0] == '0':
        return '0'
    
    # 문자열로 이어 붙이기
    return ''.join(numbers)
