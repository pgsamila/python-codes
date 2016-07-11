from itertools import groupby

f = open('output.txt','w')

for i in range(int(raw_input())):
    mylist=[]
    a=[]

    k = 0
    max = 0
    for j in range(int(raw_input())):
        b = raw_input().strip()
        n = b
        n = n.replace(" ","")
        a.append(''.join(k for k, g in groupby(sorted(n))))
        a.sort()
        c=[]
        c.append(b)
        c.append(len(a[k]))
        #print(c)
        k = k+1
        mylist.append(c)



    mylist.sort(key=lambda t:t[0] )

    mylist.sort(key=lambda t: t[1], reverse=True)

    print('Case #'+str(i+1)+': '+str(mylist[0][0]) )

    f.write('Case #'+str(i+1)+': '+str(mylist[0][0]))

f.close()