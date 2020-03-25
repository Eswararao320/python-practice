from itertools import groupby
def str1_con(string):
    string_grpby=groupby(string)
    string=""
    for i,j in string_grpby:
        list1_j=list(j)
        if len(list1_j)==1:
            string+=i
        else:
            string+="{}{}".format(len(list1_j),i)
    print(string)
n=int(input())
s=0
c=0
for i in range(n):
    str1=input()
    if str1.isalpha():
        str1_con(str1)
    else:
        for i in range(len(str1)):
            if str1[i].isdigit():
                s=s*10+int(str1[i])
            elif s!=0:
                for j in range(s):
                    print(str1[i],end='')
                    s=0
            else:
                print(str1[i],end='')
        print()
        
