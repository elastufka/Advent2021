import numpy as np

def fire_probe(x0,y0,target_area):
    x,y,max_y=0,0,0
    xv,yv=x0,y0
    while not (x in range(target_area[0],target_area[1]+1) and y in range(target_area[2],target_area[3]+1)):
        if x>target_area[1]+1 or y <target_area[2]+1:
            #print('target missed!')
            return np.nan
        #do a step
        x+=xv
        if xv != 0:
            xv-=np.sign(x)*1
        y+=yv
        if y>max_y:
            max_y=y
        yv-=1

    return max_y
    
def fire_all(xmin,xmax,ymin,ymax,target_area):
    '''bit hacky but quick to code up'''
    max_y,nhits=0,0
    for x in range(xmin,xmax):
        for y in range(ymin,ymax):
            maxy=fire_probe(x,y,target_area)
            if not np.isnan(maxy):
                #print(x,y)
                nhits+=1
                if maxy>max_y:
                    max_y=maxy
    return max_y,nhits

if __name__ == "__main__":
    
    highest_y,num_v0=fire_all(1,250,-250,250,[70,96,-179,-124])
    print("Part 1 answer: ",int(highest_y))
    print("Part 2 answer: ",int(num_v0))
    
