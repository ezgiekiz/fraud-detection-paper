import random
import numpy as np
import sys
import os

foldname=sys.argv[1]
os.makedirs(foldname,exist_ok=True)
np.random.seed(seed=int(foldname))
allidx=np.asarray(range(1,486))
np.random.shuffle(allidx)
print(len(allidx))
trlist=allidx[0:385]
#print(trlist,len(trlist))
with open(foldname+'/train', 'w') as fp:
    fp.write('\n'.join(np.char.mod('%d', trlist))+'\n')

vallist=allidx[385:385+50]
#print(vallist,len(vallist))
with open(foldname+'/val', 'w') as fp:
    fp.write('\n'.join(np.char.mod('%d', vallist))+'\n')


telist=allidx[385+50:]
with open(foldname+'/test', 'w') as fp:
    fp.write('\n'.join(np.char.mod('%d', telist))+'\n')






