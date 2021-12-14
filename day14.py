import numpy as np
from collections import Counter

#don't construct the chain, that's a waste of time! just count pairs and elements
def day14(poly_start,pairs,nsteps=2):
    chain_start,chain_end=poly_start[0],poly_start[-1]
    #print(chain_start,chain_end)
    n_elems={p:0 for p in np.unique(list(pairs.values()))}
    n_pairs={p:0 for p in pairs.keys()}
    current_pairs=[poly_start[i:i+2] for i in range(len(poly_start)-1)]
    #don't do the insertion but count the number of pairs that end up in the next layer
    fp=[c[0]+pairs[c] for c in current_pairs]
    sp=[pairs[c]+c[1] for c in current_pairs]
    fp.extend(sp) #these are the pairs (order doesn't matter) that go into the next round
    n_next_steps=Counter(fp)
    for i in range(nsteps-1):
        for p in n_next_steps:
            n_pairs[p]+=n_next_steps[p] #add existing pairs to counter
        #perform 'insertion'
        #fp=[c[0]+pairs[c] for c in n_next_steps for j in range(n_next_steps[c])]
        #sp=[pairs[c]+c[1] for c in n_next_steps for j in range(n_next_steps[c])]
        # ^^ this is slow! just ad the numbers directly to the counter!
        #for each pair, get the 2 new keys
        n_new={p:0 for p in pairs.keys()}
        for c in n_next_steps:
            k1=c[0]+pairs[c]
            k2=pairs[c]+c[1]
            n_new[k1]+=n_next_steps[c]
            n_new[k2]+=n_next_steps[c]
        n_next_steps=Counter(n_new)
        #fp.extend(sp) #these are the pairs (order doesn't matter) that go into the next round
        #n_next_steps=Counter(fp)
    #now count the elements - all are being double counted except letters at beginning and end!
    #which will always be the same
    for k in list(n_elems.keys()):
        n_elems[k]=np.sum([n_next_steps[p]*p.count(k) for p in n_next_steps.keys() if k in p])/2 #gets it wrong for doubles! eg. CC
        if k == chain_start or k == chain_end:
            n_elems[k]+=.5
    sorted_elems={k:v for v,k in sorted(zip(n_elems.values(),n_elems.keys()))}
    return sorted_elems[list(sorted_elems.keys())[-1]]-sorted_elems[list(sorted_elems.keys())[0]]
    
if __name__ == "__main__":
    
    pairs = {}
    for line in open('input_day14.txt').read().splitlines():
        try:
            s,e = line.split(' -> ')
            pairs.setdefault(s,e)
        except ValueError:
            if line !='':
                poly_start=line
    print("Part 1 answer: ",int(day14(poly_start,pairs,nsteps=10)))
    print("Part 2 answer: ",int(day14(poly_start,pairs,nsteps=40)))
    
