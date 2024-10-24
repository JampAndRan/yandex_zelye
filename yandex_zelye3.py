n=int(input())
list_graf=[[0]*n for i in range(n)]
lst_zel=[]


def repl(replicant, lst_zel):
    global count1
    global count2
    for key in lst_zel[replicant - 2].keys():
        if key == 1:
            count1 += lst_zel[replicant - 2][1]
        elif key == 2:
            count2 += lst_zel[replicant - 2][2]
        else:
            for i in range(lst_zel[replicant - 2][key]):
                if key-1 in list_cycles:
                    count1=0
                    count2=0
                    return
                repl(key-1, lst_zel)




for i in range (n-2):
    dct={}
    l_p=[int(j) for j in input().split()]
    for k in range(1,len(l_p)):
        list_graf[i+2][l_p[k]-1]=1
        if l_p[k] in dct:
            dct[l_p[k]]+=1
        else:
            dct[l_p[k]] = 1
    lst_zel.append(dct)


for k in range(n):
    for i in range(n):
        for j in range(n):
            list_graf[i][j]=list_graf[i][j] or (list_graf[i][k]and list_graf[k][j])

list_cycles=[]
for p in range(2,n):
    for k in range(p,n):
        if list_graf[p][k]==1 and list_graf[k][p]==1 :
            list_cycles.append(p)
            list_cycles.append(k )

llst=[]


for t in range(2,n):
    dctt = {}
    if t in list_cycles:
        dctt[1] = 0
        dctt[2] = 0
        llst.append(dctt)
        continue
    else:
        count1=0
        count2=0
        repl(t, lst_zel)
        dctt[1] = count1
        dctt[2] = count2
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


