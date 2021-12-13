import numpy as np

def day13_part1(fname='test_input_day13.txt',first_fold_dir=np.flipud,first_fold_coord=7):
    coords=[]
    for line in open(fname).read().splitlines():
        try:
            x,y = line.split(',')
            coords.append([int(x),int(y)])
        except ValueError:
            break
    coords=np.array(coords)
    paper_size=[np.max(coords[:,1])+1,np.max(coords[:,0])+1]
    paper=np.zeros(paper_size)
    for x,y in coords:
        paper[y,x]=1
    if first_fold_dir==np.flipud:
        top_half=paper[:first_fold_coord]
        bottom_half=paper[first_fold_coord+1:]
    else: #other direction, fliplr
        top_half=paper[:,:first_fold_coord]
        bottom_half=paper[:,first_fold_coord+1:]
    folded=top_half+first_fold_dir(bottom_half)
    folded[folded >0]=1
    return folded,np.sum(folded)
    
def day13_part2(fname='test_input_day13.txt'):
    coords,folds=[],[]
    for line in open(fname).read().splitlines():
        try:
            x,y = line.split(',')
            coords.append([int(x),int(y)])
        except ValueError:
            if line.startswith('fold'):
                folds.append([line[line.find("=")-1:line.find("=")],int(line[line.find("=")+1:])])
            else:
                continue
    coords=np.array(coords)
    paper_size=[np.max(coords[:,1])+2,np.max(coords[:,0])+1] #+2 in x because native size is even number which should not be allowed!
    print(paper_size)
    paper=np.zeros(paper_size)
    #paper = np.zeros((np.max(coords, axis = 0)[::-1]+1))
    for x,y in coords:
        paper[y,x]=1

    for f,n in folds:
        if f=='y':
            folded=paper[0:n,:]+np.flip(paper[n+1:,:],axis=0)
        else:
            folded=paper[:,0:n]+np.flip(paper[:,n+1:],axis=1)

        folded[folded >0]=1
        paper=folded
    return paper, coords,folds
    
if __name__ == "__main__":
    
    code,n=day13_part1('input_day13.txt',first_fold_dir=np.fliplr,first_fold_coord=655)
    print("Part 1 answer: ",int(n))
    code,coords,folds=day13_part2('input_day13.txt')
    plt.imshow(code)
    
