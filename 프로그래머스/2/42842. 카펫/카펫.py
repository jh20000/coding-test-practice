
def solution(brown, yellow):
    for h in range(1, yellow +1):
        if yellow % h == 0:
            w = yellow // h
            total_w = w + 2
            total_h = h + 2
            total_a = total_h * total_w
            if total_a == yellow + brown:
                return [total_w, total_h]