the_file = open('happiness_seg.txt','r')  
txt = the_file.read()
# to build a blank dict
data = {}
# to get rid of '\n'
lines = txt.split('\n')
for line in lines:
    tempt = line.split(' ')  # transfer each line to separate words, forming list 
    for ci_zu in tempt:
        if len(ci_zu) == 12:   # to ensure the length of the words
            if ci_zu in data:
                data[ci_zu] += 1    
            else:
                data[ci_zu] = 1    # in dict data, keys are the words required, values frequencies
        

the_file.close()


def sort_by_value(d):      # to sort out the 10 most frequent words
    items = d.items()
    rev_items = [[v[1],v[0]]for v in items]
    rev_items.sort(reverse = True)
    step = 0
    while step < 10:
        print rev_items[step][1], rev_items[step][0]
        step += 1

sort_by_value(data)


