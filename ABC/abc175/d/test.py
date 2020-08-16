import sys
from numpy import*
def main(n,k,p,c):
    m=-10**12
    for i in range(n):
        s=i
        t=1
        x=c[s]
        while p[s]-1!=i:
            s=p[s]-1
            t+=1
            x+=c[s]
        if x>0:
            a=(k//t-1)*x
            if a>m:m=a
            s=i
            for _ in range(k%t+t):
                s=p[s]-1
                a+=c[s]
                if a>m:m=a
        else:
            a=0
            s=i
            for _ in range(min(k,t)):
                s=p[s]-1
                a+=c[s]
                if a>m:m=a
    return m
if sys.argv[-1]=='ONLINE_JUDGE':
  from numba.pycc import CC
  cc=CC('my_module')
  cc.export('main','i8(i8,i8,i8[:],i8[:])')(main)
  cc.compile()
  exit()
from my_module import main
(n,k),p,c=[int_(t.split())for t in open(0)]

import os
import sys
#import numpy as np
 
def solve(N, X, D):
    return 
 
# >>> numba compile >>>
numba_config = [
    [solve, "i8(i8,i8,i8)"],
]
if sys.argv[-1] == "ONLINE_JUDGE":
    from numba import njit
    from numba.pycc import CC
    cc = CC("my_module")
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature)(func)
        cc.export(func.__name__, signature)(func)
    cc.compile()
    exit()
elif os.name == "posix":
    exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
else:
    from numba import njit
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature, cache=True)(func)
    print("compiled!", file=sys.stderr)
# <<< numba compile <<<
