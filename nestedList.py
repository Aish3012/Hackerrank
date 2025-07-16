lst=[]
score_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        score_list.append(score)

sorted_score_list=sorted(list(set(score_list)))
second_lowest=sorted_score_list[1]
name_list=[]
for i in range(len(lst)):
    if second_lowest in lst:
        name=lst[i][0]
        name_list.append(name)
name_list.sort()
for i in name_list:
    print(i)

    
      


        