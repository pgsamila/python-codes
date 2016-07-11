from operator import itemgetter

test = int(input())
f = open('output.txt','w')

for z in range(test):
    people = int(input())
    plist = []

    for o in range(people):
        name =  raw_input()
        k = []
        namelist = list(name.replace(' ',''))
        #print(namelist)

        namelist = set(namelist)
        #print(namelist)
        k.append(name)
        #print(k)
        k.append(len(namelist))
        #print(k)
        plist.append(k)
        print(plist)
    plist.sort(key = lambda t:t[0])
    #print(plist)
    plist.sort(key=lambda t: t[1] , reverse=True)
    print(plist)
    #print('Case #' + str(z + 1) + ': ' + str(plist[0][0]))



    # 2
    # 3
    # ADAM
    # BOB
    # JOHNSON
    # 2
    # A
    # AB
    # C
    # DEF