import pandas as pd
import numpy as np
import numpy.ma
from numpy.ma import MaskError

class Bingo():
    def __init__(self,textfile,let_the_squid_win=False):
        moves,boards=self.read_input(textfile)
        self.moves=moves
        self.boards=boards
        self.let_the_squid_win=let_the_squid_win
        print(len(self.boards))
        
    def read_input(self,textfile):
        with open(textfile) as f:
            lines=f.readlines()
            moves=lines[0][:-3].split(',')
            moves=[int(m) for m in moves]
        nboards=(len(lines)-1)//5
        #print(nboards)
        df=pd.read_csv(textfile,header=None,skiprows=1)
        boards=[df[0][i*5:5*(i+1)].values.tolist() for i in range(nboards)]
        for i,board in enumerate(boards):
            blist=[row.strip().replace('  ',' ').split(' ') for row in board]
            blon=[int(b) for row in blist for b in row]
            try:
                barr=np.ma.array(blon,mask=np.zeros((5,5))).reshape((5,5))
                boards[i]=barr
            except MaskError:
                boards=boards[:i]
                break
        return moves,boards

    def draw_number(self,move):
        for i,board in enumerate(self.boards):
            num_loc=np.where(board == move)
            #print(num_loc[0],num_loc[1],num_loc[0].size)
            if num_loc[0].size !=0:
                cmask=self.boards[i].mask
                cmask[num_loc[0],num_loc[1]] = True
                self.boards[i].mask=cmask
                
    def check_win(self,wins):
        winning_board=0
        for i,board in enumerate(self.boards):
            if i not in wins:
                bmask=board.mask
                rowsums=np.sum(bmask,axis=0)
                colsums=np.sum(bmask,axis=1)
                if 5 in rowsums or 5 in colsums:
                    wins.append(i)
                    winning_board=board
                    if not self.let_the_squid_win:
                        break #doesn't allow for tie
                    else: #multiple boards can win at once
                        print(f'board {i} has won!')
        return wins,winning_board

    def calc_score(self,winning_move,winning_board):
        #sum of all unwinning numbers times number of winning move
        return winning_move*np.sum(winning_board)

    def play_bingo(self):
        wins=[-1]
        for move in self.moves:
            self.draw_number(move)
            #print(move)
            wins,winning_board=self.check_win(wins)
            if type(winning_board) == np.ma.masked_array and self.let_the_squid_win == False:
                score=self.calc_score(move,winning_board)
                break
            elif len(np.unique(wins))==len(self.boards)+1: #or move= last_move
                print(move,win,winning_board)
                score=self.calc_score(move,winning_board)
                break
        return wins,winning_board,score

if __name__ == "__main__":
    win,winning_board,score=Bingo('input_day4.txt').play_bingo()
    print("Part 1 answer: ",score)
    win,winning_board,score=Bingo('input_day4.txt',let_the_squid_win=True).play_bingo()
    print("Part 2 answer: ",score)
    
