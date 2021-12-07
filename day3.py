import pandas as pd
import numpy as np
from operator import lt, ge

def day3_part1(blist,blen=5):
    gamma,epsilon=[],[]
    for i in range(blen):
        g=np.argmax(np.bincount([str(b)[i] for b in blist])) #most common bit
        gamma.append(str(g))
        epsilon.append(str(1-g))
    gamma_dec=int(''.join(gamma),2)
    epsilon_dec=int(''.join(epsilon),2)
    return gamma_dec*epsilon_dec

def filter_values(blist,i,fn=ge):
    ones=[b for b in blist if b[i] == '1']
    zeros=[b for b in blist if b[i] == '0']
    if fn(len(ones),len(zeros)):
        blist=ones
    else:
        blist=zeros
    return blist

def day3_part2(blist,blen=5):
    o2=blist.copy()
    co2=blist.copy()
    for i in range(blen):
        o2=filter_values(o2,i)
        if len(o2)==1:
            break
    for i in range(blen):
        co2=filter_values(co2,i,fn=lt)
        #print(i,co2)
        if len(co2)==1:
            break
    return int(o2[0],2)*int(co2[0],2)

if __name__ == "__main__":
    day3_input=pd.read_csv('input_day3.txt',header=None,converters={0: lambda x: str(x)})
    day3list=day3_input[0].to_list()
    print("Part 1 answer: ",day3_part1(day3list,blen=12))
    print("Part 2 answer: ",day3_part2(day3list,blen=12))
    
