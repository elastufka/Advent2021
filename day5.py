import pandas as pd
import numpy as np

def overlap(input_list):
    '''produce the diagram array'''
    arr=np.array(input_list)
    xmax=np.max([arr.T[0],arr.T[2]])+1
    ymax=np.max([arr.T[1],arr.T[3]])+1
    print(xmax,ymax)
    diagram=np.zeros((xmax,ymax))
    #fill diagram
    for x1,y1,x2,y2 in input_list:
        #print((x1,y1),(x2,y2))
        if x1 == x2: #vertical
            diagram[min([y1,y2]):max([y1,y2])+1,x1]+=1
            #print(diagram)
        elif y1==y2: #horizontal
            diagram[y1,min([x1,x2]):max([x1,x2])+1]+=1
            #print(diagram)
    return diagram
    
def overlap2(input_list):
    '''produce the diagram array'''
    arr=np.array(input_list)
    xmax=np.max([arr.T[0],arr.T[2]])+1
    ymax=np.max([arr.T[1],arr.T[3]])+1
    print(xmax,ymax)
    diagram=np.zeros((xmax,ymax))
    #fill diagram
    for x1,y1,x2,y2 in input_list:
        #print((x1,y1),(x2,y2))
        if x1 == x2: #vertical
            diagram[min([y1,y2]):max([y1,y2])+1,x1]+=1
            #print(diagram)
        elif y1==y2: #horizontal
            diagram[y1,min([x1,x2]):max([x1,x2])+1]+=1
            #print(diagram)
        else: #diagonal at 45 degrees
            #print((x1,y1),(x2,y2))
            #change so x1 is paired with min(y1,y2)
            if y2 < y1:
                #print('swap')
                x1,y1,x2,y2=x2,y2,x1,y1
                #print((x1,y1),(x2,y2))
            y,yend=y1,y2
            if x1>x2: #backward diag
                x=x1
                minus=True
            elif x2>x1: #backward
                x=x1
                minus=False
            while y <=yend:
                diagram[y,x]+=1
                if minus:
                    x-=1
                else:
                    x+=1
                y+=1
    return diagram
    
if __name__ == "__main__":
    with open('input_day5.txt') as f:
        lines=f.readlines()
    str_input=[]
    for l in lines:
        str_input.append(l[:-1].split(','))
    day5_input=[[int(s) for s in line] for line in str_input]
    
    diagram=overlap(day5_input)
    print("Part 1 answer: ",diagram[diagram >=2].shape)
    diagram=overlap2(day5_input)
    print("Part 2 answer: ", diagram[diagram>=2].shape)
    
