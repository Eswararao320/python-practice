import textwrap
x = int(input())
p = input()
q = textwrap.TextWrapper(width = x)
w = q.wrap(text=p)
for i in w[:-1]:
    li = list(i.split(" "))
    space_occupied = 0
    for j in li:
        space_occupied += len(j)
    remaining_space = x - space_occupied
    if len(li) > 1:
        p,q = divmod(remaining_space,len(li)-1)
        lis = []
        for j in li[:-1]:
            j = j+" "*p
            lis.append(j)
        lis.append(li[-1])
        for j in range(len(lis)-1):
            if q == 0:
                break
            lis[j] = lis[j]+" "
            q = q-1
        print("".join(lis))
print(w[-1].ljust(x," "))
