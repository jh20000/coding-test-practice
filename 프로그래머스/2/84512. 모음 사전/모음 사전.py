from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    all_words = []
    
    for i in range(1, 6):  # 단어 길이: 1 ~ 5
        #repeat product 
        for comb in product(alpha, repeat=i):
            all_words.append(''.join(comb))
    
    all_words.sort()  # 사전순 정렬
    
    return all_words.index(word) + 1  # 1-based index
