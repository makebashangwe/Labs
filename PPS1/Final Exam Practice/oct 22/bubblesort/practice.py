def b_sort(scores):
    n = len(scores)
    for i in range(n):
        for j in range(0,n-i-1):
            if scores[j] > scores[j+1]:
                scores[j],scores[j+1] = scores[j+1], scores[j]
    
    return scores




scores = [72, 95, 85, 63, 87, 78, 55, 91, 89, 70]
print(b_sort(scores))
sorted_scores = b_sort(scores)
top_three = sorted_scores[-3:]
print(f"Top three scores: ", top_three)

