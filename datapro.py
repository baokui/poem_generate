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
        k = 0
        for i in range(len(data)):
            s = data[i].split(',')
            if len(s)!=4:
                continue
            k+=1
            title,author,content = s[0][1:-1],s[2][1:-1],s[3][1:-1]
            t = '::'.join([title,author,content])
            S.append(t)
            if len(S)%1000==0:
                print(len(S))
        print('get %d poems from file %s'%(k,file))
    print('total number is %d'%len(S))
    random.shuffle(S)
    with open(path_target,'w') as f:
        f.write('\n'.join(S))
def separate(path_source,path_target_shi,path_target_ci):
    syms = '，。'
    def splitting(s0):
        s = []
        i0 = 0
        i1 = 0
        while i1<len(s0):
            if s0[i1] in syms and i1>i0:
                s.append(s0[i0:i1])
                i0 = i1+1
                i1 = i1+1
            else:
                i1 += 1
        s.append(s0[i0:i1])
        return s
    def check(s):
        n = [len(ss) for ss in s]
        if max(n)!=min(n):
            return False
        return True
    with open(path_source,'r') as f:
        data = f.read().strip().split('\n')
    s_shi = []
    s_ci = []
    for i in range(len(data)):
        if i%1000==0:
            print(i,len(data))
        t = data[i].split('::')
        s = splitting(t)
        if check(s):
            s_shi.append(t)
        else:
            s_ci.append(t)
    with open(path_target_shi,'w') as f:
        f.write('\n'.join(s_shi))
    with open(path_target_ci,'w') as f:
        f.write('\n'.join(s_ci))

if __name__=='__main__':
    mode = sys.argv[1]
    if mode == 'rawPeom':
        path_source, path_target = sys.argv[2:4]
        getRaw(path_source,path_target)
    if mode == 'seprate':
        path_source, path_target_shi,path_target_ci = sys.argv[2:5]
        separate(path_source, path_target_shi,path_target_ci)
