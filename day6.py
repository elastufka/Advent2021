import pandas as pd
import numpy as np

class Lanternfish:
    def __init__(self,internal_timer=3):
        self.state=internal_timer
        self.ncycles=0
        
    def countdown(self):
        if self.state == 0:
            self.ncycles +=1
            self.state = 6
        else:
            self.state -=1
        return self.state
        
def fish_sim(initial_state, days):
    fish=[Lanternfish(internal_timer=s) for s in initial_state]
    for d in range(days):
        fish_state=[f.countdown() for f in fish]
        #if there's a six, append an 8 at the end
        n_spawned=np.where(np.array(fish_state) == 0)[0].size
        #print(n_spawned)
        for n in range(n_spawned):
            fish.append(Lanternfish(internal_timer=9)) #plus one because countdown shouldn't begin when it spawns
        #print(fish_state,len(fish))
    return fish_state, len(fish)-n_spawned #since I initialize them early...
    
def fast_fish_sim(initial_state, days):
    fish_state=np.array(initial_state)
    for d in range(days):
        #if there's a six, append an 8 at the end
        n_spawned=np.count_nonzero(fish_state==0)
        fish_state=np.append(fish_state,9+np.zeros(n_spawned)) #plus one because countdown shouldn't begin when it spawns
        fish_state[fish_state == 0] = 7
        fish_state-=1
        if d % 10 == 0:
            print(d)
        #print(fish_state,len(fish))
    return fish_state, len(fish_state) #since I initialize them early...
    
if __name__ == "__main__":
    full_input=[1,4,3,3,1,3,1,1,1,2,1,1,1,4,4,1,5,5,3,1,3,5,2,1,5,2,4,1,4,5,4,1,5,1,5,5,1,1,1,4,1,5,1,1,1,1,1,4,1,2,5,1,4,1,2,1,1,5,1,1,1,1,4,1,5,1,1,2,1,4,5,1,2,1,2,2,1,1,1,1,1,5,5,3,1,1,1,1,1,4,2,4,1,2,1,4,2,3,1,4,5,3,3,2,1,1,5,4,1,1,1,2,1,1,5,4,5,1,3,1,1,1,1,1,1,2,1,3,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,4,5,1,3,1,4,4,2,3,4,1,1,1,5,1,1,1,4,1,5,4,3,1,5,1,1,1,1,1,5,4,1,1,1,4,3,1,3,3,1,3,2,1,1,3,1,1,4,5,1,1,1,1,1,3,1,4,1,3,1,5,4,5,1,1,5,1,1,4,1,1,1,3,1,1,4,2,3,1,1,1,1,2,4,1,1,1,1,1,2,3,1,5,5,1,4,1,1,1,1,3,3,1,4,1,2,1,3,1,1,1,3,2,2,1,5,1,1,3,2,1,1,5,1,1,1,1,1,1,1,1,1,1,2,5,1,1,1,1,3,1,1,1,1,1,1,1,1,5,5,1
    ]
    
    states,nfish=fish_sim(full_input,80)
    print("Part 1 answer: ",nfish)
    #_,nfish=fast_fish_sim(full_input,256) #don't do this in real time... it isn't fast at all!
    #print("Part 2 answer: ", nfish)
    
