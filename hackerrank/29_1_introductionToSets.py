def average(array):
    set1=set(array)
    m=len(set1)
    total=0
    for i in set1:
        total+=i
    avg=float(total/m)
    final=round(avg,3)
    return final

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)