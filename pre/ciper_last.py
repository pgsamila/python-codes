order = ' etaoinrshdlcumwf'

input = raw_input()
text = raw_input()

index = dict([ (y,x) for (x,y) in enumerate(order) ])

output = sorted(input, cmp=lambda x,y: index[x] - index[y])
    
print(output)