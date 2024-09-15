import re


inheritance, L = {}, {}
while s := input():
    if s.find('class') == 0:
        ancestors = []
        match = re.search(r'\s.*\(.*\)', s)

        if match:
            declaration = match[0][1:]
            class_name = re.search(r'.*\(', declaration)[0][:-1].strip()
            ancestors = re.search(r'\(.*\)', declaration)[0][1:-1].replace(' ', '').split(',')
        else:
            class_name = re.search(r'\s.*:', s)[0][1:-1].strip()

        inheritance[class_name] = ancestors
        L[class_name] = [class_name]

        if ancestors:
            merge = [L[ancestor] for ancestor in ancestors] + [ancestors]
            
            while True:
                merge = [mro for mro in merge if mro]
                if not merge:
                    break
                
                for mro in merge:
                    candidate = mro[0]
                    if [s for s in merge if candidate in s[1:]]:
                        candidate = None
                    else:
                        break

                if not candidate:
                    break
                else:
                    L[class_name].append(candidate)
                    for mro in merge:
                        if mro[0] == candidate:
                            del mro[0]

            if any(merge):
                print('No')
                break
else:
    print('Yes')


                        
        
