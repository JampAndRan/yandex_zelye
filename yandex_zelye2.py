n=int(input())
lst_zel=[]


def repl(replicant, lst_zel):
    global sum_x
    sum_x-=1
    global count1
    global count2
    try:
        for key in lst_zel[replicant - 3].keys():
            if sum_x < 0:
                count1 = 0
                count2 = 0
                return
            if key == 1:
                count1 += lst_zel[replicant - 3][1]
            elif key == 2:
                count2 += lst_zel[replicant - 3][2]
            else:
                for i in range(lst_zel[replicant - 3][key]):
                    repl(key, lst_zel)

    except RuntimeError:
        count1 = 0
        count2 = 0


sum=0
for i in range (n-2):
    dct={}
    l_p=[int(j) for j in input().split()]
    sum+=l_p[0]
    for k in range(1,len(l_p)):
        if l_p[k] in dct:
            dct[l_p[k]]+=1
        else:
            dct[l_p[k]] = 1
    lst_zel.append(dct)

llst=[]

for n in range(len(lst_zel)):
    dctt={}
    count1=0
    count2=0
    sum_x = sum + 1
    repl(n+3,lst_zel)
    dctt[1]=count1
    dctt[2]=count2
    llst.append(dctt)



q=int(input())

for i in range(q):
    zapros=[int(j) for j in input().split()]
    u=llst[zapros[2]-3][1]
    v=llst[zapros[2]-3][2]
    if u==0 and v==0:
        print(0, end='')
        continue
    if zapros[0]>=u and zapros[1]>=v:
        print(1, end='')
    else:
        print(0, end='')

