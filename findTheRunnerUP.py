if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
lst=list(arr)
sorted_list=sorted(list(set(lst)))
print(sorted_list[-2])