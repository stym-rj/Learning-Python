teams=int(input())
s=input()
scores=s.split()

list_scores=[]
for i in scores:
    list_scores.append(i)

list_scores.sort()

length=len(list_scores)
for i in range(length-1):
    if list_scores[length-2-i]==list_scores[length-1-i]:
        continue
    else:
        print(list_scores[length-2-i])
        break