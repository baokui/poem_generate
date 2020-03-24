import os
import random
import sys
def getRaw(path_source,path_target):
    files = os.listdir(path_source)
    S = []
    for file in files:
        if '.csv' not in file:
            continue
        with open(os.path.join(path_source,file),'r') as f:
            data = f.read().strip().split('\n')[1:]
        print(file)
        for i in range(len(data)):
            s = data[i].split(',')
            title,author,content = s[0][1:-1],s[2][1:-1],s[3][1:-1]
            t = '::'.join([title,author,content])
            S.append(t)
            if len(S)%1000==0:
                print(len(S))
    print('total number is %d'%len(S))
    random.shuffle(S)
    with open(path_target,'w') as f:
        f.write('\n'.join(S))
if __name__=='__main__':
    mode = sys.argv[1]
    if mode == 'rawPeom':
        path_source, path_target = sys.argv[2:4]
        getRaw(path_source,path_target)
