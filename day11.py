import numpy as np

def day11_part1(test_input):
    s=0
    steps=100
    nflashes=0
    while s < steps:
        #if s >=50:
            #print(s,nflashes)
            #print(test_input)
        test_input+=1 #step 1
        nines=np.where(test_input >= 9)
        if nines[0].size > 0:
            #print(test_input)
            s+=1

            #test_input+=1 #start step 2 - there are now 9's and 10's
            #print(test_input)
            new_nines=np.where(test_input > 9)
            #print(new_nines)
            while new_nines[0].size >0:
                for x,y in zip(new_nines[0],new_nines[1]):
                    #print('x,y:',x,y)
                    test_input[x,y]*=-100 #so you know it flashed
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if x+i >=0 and y+j >=0 and x+i <test_input.shape[0] and y+j <test_input.shape[1]:
                                test_input[x+i,y+j]+=1
                                #print(x+i,y+j)
                new_nines=np.where(test_input >= 10) #can also skip from say 9-11... doesn't necessarily pass through 10!
            test_input[test_input >9] = 0
            test_input[test_input <0] = 0
            nflashes +=(np.product(test_input.shape) - np.count_nonzero(test_input))
        else:
            #test_input+=1
            s+=1
    return nflashes
    
def day11_part2(test_input,niter=1000):
    s=0
    nflashes=0
    while s < niter:
        if np.count_nonzero(test_input)!=0:
            test_input+=1 #step 1
            nines=np.where(test_input >= 9)
            if nines[0].size > 0:
                #print(test_input)
                s+=1

                #test_input+=1 #start step 2 - there are now 9's and 10's
                #print(test_input)
                new_nines=np.where(test_input > 9)
                #print(new_nines)
                while new_nines[0].size >0:
                    for x,y in zip(new_nines[0],new_nines[1]):
                        #print('x,y:',x,y)
                        test_input[x,y]*=-100 #so you know it flashed
                        for i in range(-1,2):
                            for j in range(-1,2):
                                if x+i >=0 and y+j >=0 and x+i <test_input.shape[0] and y+j <test_input.shape[1]:
                                    test_input[x+i,y+j]+=1
                                    #print(x+i,y+j)
                    new_nines=np.where(test_input >= 10) #can also skip from say 9-11... doesn't necessarily pass through 10!
                test_input[test_input >9] = 0
                test_input[test_input <0] = 0
                nflashes +=(np.product(test_input.shape) - np.count_nonzero(test_input))
            else:
                s+=1
        else:
            break
    return s,nflashes
    
if __name__ == "__main__":
    
    print("Part 1 answer: ",day11_part1(day11_input))
    n,_day11_part2(day11_input,niter=2000)
    print("Part 2 answer: ",n)
    
