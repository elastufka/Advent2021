import pandas as pd

def day2_part1(day2_input):
    x,y=0,0
    #direction can only be forward, up, down
    day2_input.replace({'forward':0},inplace=True)
    day2_input.replace({'up':-1},inplace=True)
    day2_input.replace({'down':1},inplace=True)
    for _,row in day2_input.iterrows():
        if row[0] == 0:
            x+=row[1]
        else:
            y+=row[0]*row[1]
    print(x,y)
    return x*y

def day2_part2(day2_input):
    x,y,aim=0,0,0
    #direction can only be forward, up, down
    day2_input.replace({'forward':0},inplace=True)
    day2_input.replace({'up':-1},inplace=True)
    day2_input.replace({'down':1},inplace=True)
    for _,row in day2_input.iterrows():
        if row[0] == 0:
            x+=row[1]
            y+=row[1]*aim
        else:
            aim+=row[0]*row[1]
    print(x,y,aim)
    return x*y

if __name__ == "__main__":
    day2_input=pd.read_csv('input_day2.txt',header=None,delimiter=' ')
    print("Part 1 answer: ",day2_part1(day2_input))
    print("Part 2 answer: ",day2_part2(day2_input))
    
