import pandas as pd

def day1_part1(input_list):
    count=0
    for i,item in enumerate(input_list[:-1]):
        if input_list[i+1] > item:
            count+=1
    return count

def day1_part2(input_series):
    count=0
    threedf=input_series.rolling(3)[0].sum().to_list()[2:]
    for i,item in enumerate(threedf[:-1]):
        if threedf[i+1] > item:
            count+=1
    return count

if __name__ == "__main__":
    day1_input=pd.read_csv('input_day1.txt',header=None)
    day1list=day1_input[0].to_list()
    print("Part 1 answer: ",day1_part1(day1list))
    print("Part 2 answer: ",day1_part2(day1_input))
    
