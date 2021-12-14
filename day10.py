import numpy as np

def illegal(line):
    is_open=[]
    for i,c in enumerate(line):
        if c in open_chars:
            is_open.append(c)
        elif c in close_chars and close_chars.index(c) == open_chars.index(is_open[-1]): #valid
            is_open.pop(-1) #it's closed so remove it
        else:
            #print(f"Expected {close_chars[open_chars.index(is_open[-1])]}, found {c} instead!")
            return scores[c]
    return 0
    

def missing(line):
    is_open,complete=[],[]
    score=0
    for i,c in enumerate(line):
        if c in open_chars:
            is_open.append(c)
        elif c in close_chars and close_chars.index(c) == open_chars.index(is_open[-1]): #valid
            is_open.pop(-1) #it's closed so remove it
    if is_open !=[]: #still got characters left
        is_open.reverse()
        for c in is_open:
            cm=close_chars[open_chars.index(c)]
            complete.append(cm)
            score*=5
            score+=cscores[cm]
        #print(''.join(complete))
        return score
        
def repair(lines):
    scores=[]
    for line in lines:
        scores.append(missing(line))
    return scores
    
if __name__ == "__main__":
    
    open_chars=['[','(','{','<']
    close_chars=[']',')','}','>']
    scores={')':3,'}':1197,']':57,'>':25137}
    cscores={')':1,']':2,'}':3,'>':4}
    
    with open('input_day10.txt') as f:
        lines=f.readlines()
        
    lscores=0
    clean_input=[]
    for line in lines:
        score=illegal(line[:-1])
        lscores+=score
        if score ==0:
            clean_input.append(line)
            
    print("Part 1 answer: ",lscores)
    ss=repair(clean_input)
    print("Part 2 answer: ",np.median(ss))
    
