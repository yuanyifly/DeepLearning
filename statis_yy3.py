#--coding:utf-8--
the_file = open('happiness_seg.txt','r') 
data = {}

for line in the_file:
    line = line.strip()
    if len(line) > 0:

        import re
        words = re.split(r'[\s]',line)
       
       
        if len(words) >= 2:
            length = len(words)
            count = 0
            while count < length-1:            
                item1 = words[count]
                item2 = words[count+1]
                
                if item2 not in ['。','，','：','；','？','?','―']:
                    item = item1 + ' ' + item2
          
                    count = count + 1
                    if item in data:
                        data[item] += 1
                    else:
                        data[item] = 1
                else:
                    count = count + 2 
        
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
