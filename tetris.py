import pygame
from pygame.locals import *
import random
import numpy
import sys

class Tetris():
    def __init__(self):
        self.Field_width = 10
        self.Field_hight = 20
        self.Field_wall = 2
        self.Field_top = 2
        self.screen = pygame.display.set_mode((1000, 660))
        self.block = [
            #null
            [[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]],
            #I
            [[[0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]],

            [[0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0]],

            [[0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]]],
            #O
            [[[0,0,0,0],
            [0,2,2,0],
            [0,2,2,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,2,2,0],
            [0,2,2,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,2,2,0],
            [0,2,2,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,2,2,0],
            [0,2,2,0],
            [0,0,0,0]]],
            #S
            [[[0,0,0,0],
            [0,3,3,0],
            [3,3,0,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,3,0,0],
            [0,3,3,0],
            [0,0,3,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [0,3,3,0],
            [3,3,0,0]],

            [[0,0,0,0],
            [3,0,0,0],
            [3,3,0,0],
            [0,3,0,0]]],
            #Z
            [[[0,0,0,0],
            [4,4,0,0],
            [0,4,4,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,0,4,0],
            [0,4,4,0],
            [0,4,0,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [4,4,0,0],
            [0,4,4,0]],

            [[0,0,0,0],
            [0,4,0,0],
            [4,4,0,0],
            [4,0,0,0]]],
            #J
            [[[0,0,0,0],
            [5,0,0,0],
            [5,5,5,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,5,5,0],
            [0,5,0,0],
            [0,5,0,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [5,5,5,0],
            [0,0,5,0]],

            [[0,0,0,0],
            [0,5,0,0],
            [0,5,0,0],
            [5,5,0,0]]],
            #L
            [[[0,0,0,0],
            [0,0,6,0],
            [6,6,6,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,6,0,0],
            [0,6,0,0],
            [0,6,6,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [6,6,6,0],
            [6,0,0,0]],

            [[0,0,0,0],
            [6,6,0,0],
            [0,6,0,0],
            [0,6,0,0]]],
            #T
            [[[0,0,0,0],
            [0,7,0,0],
            [7,7,7,0],
            [0,0,0,0]],

            [[0,0,0,0],
            [0,7,0,0],
            [0,7,7,0],
            [0,7,0,0]],

            [[0,0,0,0],
            [0,0,0,0],
            [7,7,7,0],
            [0,7,0,0]],

            [[0,0,0,0],
            [0,7,0,0],
            [7,7,0,0],
            [0,7,0,0]]],]
        self.Field = [[8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
                    [8,8, 8,8,8,8,8,8,8,8,8,8, 8,8],
                    [8,8, 8,8,8,8,8,8,8,8,8,8, 8,8]
                    ]
        self.block_colors = {
            0: (255, 255, 255),
            1: (0, 255, 255),
            2: (255, 255, 0),
            3: (0, 255, 0),
            4: (255, 0, 0),
            5: (0, 0, 255),
            6: (255, 128, 0),
            7: (127, 0, 255),
            8: (128, 128, 128),
            9: (0,111,111),
            10: (153, 255, 255),
            20: (255, 255, 153),
            30: (153, 255, 153),
            40: (255, 153, 153),
            50: (153, 153, 255),
            60: (255, 204, 153),
            70: (204, 153, 255)}
        
        self.initial_x = 3
        self.initial_y = 0
        self.x = self.initial_x
        self.y = self.initial_y
        self.next = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.tonextCount = 0
        self.dir = 0
        self.next_display = 6
        self.score = 0
        self.line = 0
        self.hold = 0
        self.useHold = False
        self.ghostY = 0
        self.count = 0
        self.game_over = False
        self.useTspin = False
        self.useTspinMini = False
        self.BackToBack = False
        self.ren = 0
        self.message = ""
        

    #nextをランダムに決める
    def nextDecide(self):
        val = [7,1,2,3,4,5,6]
        loop = int(numpy.size(self.next) / 7)
        for i in range (loop):
            if self.next[i * 7] == 0:
                random.shuffle(val)
                for j in range (7):
                    self.next[i * 7 + j] = val[j]

    #nextを更新
    def nextTONext(self):
        for i in range (numpy.size(self.next)-1):
            self.next[i] = self.next[i+1]
        self.next[numpy.size(self.next)-1] = 0
        self.tonextCount += 1
        if self.tonextCount == 7:
            self.nextDecide()
            self.tonextCount = 0

    #方向と距離を引数とした、ブロックの移動
    def minoMoving(self, move, pwr):
        for i in range (4):
            for j in range (4):
                target = self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall]
                if target == self.block[self.next[0]][self.dir][i][j]:
                    self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall] = 0
        if self.MoveCheck(move, pwr, self.x, self.y, self.dir):
            if move == 0:
                self.y += -pwr
            elif move == 1:
                self.x += pwr
            elif move == 2:
                self.y += pwr
            elif move == 3:
                self.x += -pwr
            self.useSpin = False
            self.minoDrawing(self.next[0], self.dir)
        elif move == 2:
            self.minoDrop()

    #自由落下
    def free_fall(self):
        self.minoMoving(2,1)

    #描画
    def draw(self):
        #mino
        for i in range (2,24):
            for j in range (14):
                rect = pygame.Rect(120+30*j,30*(i - self.Field_top),30,30)
                self.screen.fill(self.block_colors[self.Field[i][j]], rect)
        #ghost
        for i in range (4):
            for j in range (4):
                if self.block[self.next[0]][self.dir][i][j] != 0:
                    rect = pygame.Rect(180+30*(self.x+j),30*(self.ghost()+i)-30,30,30)
                    self.screen.fill(self.block_colors[10* self.next[0]], rect)
        #line
        for i in range(9):
            pygame.draw.line(self.screen, (200,200,200), (210+30*i, 0), (210+30*i, 600), 1)
        for i in range(19):
            pygame.draw.line(self.screen, (200,200,200), (180, i*30 + 30), (480, i*30 + 30), 1)
        #Score
        self.score_draw()

    #Ghost表示
    def ghost(self):
        self.ghostY = 0
        while(self.MoveCheck(2,1,self.x, self.y, self.dir, 0,self.ghostY)):
            self.ghostY += 1
        return self.ghostY + self.y

    #ブロックの位置情報を更新して描画
    def minoDrawing(self, m, d):
        for i in range(4):
            for j in range(4):
                if self.block[m][d][i][j] != 0:
                    self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall] = self.block[m][d][i][j]
        self.draw()
    
    #衝突判定
    def MoveCheck(self, direction, power, self_x, self_y, dir, srsx=0, srsy=0):
        diry = 0
        dirx = 0
        checked = [False, False, False, False]
        for i in range(4):
            for j in range(4):
                if direction == 0:
                    diry = i
                    dirx = j
                elif direction == 1:
                    diry = j
                    dirx = 3-i
                elif direction == 2:
                    diry = 3-i
                    dirx = j
                elif direction == 3:
                    diry = j
                    dirx = i
                if self.block[self.next[0]][dir][diry][dirx] != 0:
                    if direction == 0:
                        if self.Field[diry + self_y - power + self.Field_top - 1 + srsy][dirx + self_x + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    elif direction == 1:
                        if self.Field[diry + self_y + self.Field_top - 1 + srsy][dirx + self_x + power + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    elif direction == 2:
                        if self.Field[diry + self_y + power + self.Field_top - 1 + srsy][dirx + self_x + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    elif direction == 3:
                        if self.Field[diry + self_y + self.Field_top - 1 + srsy][dirx + self_x - power + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    checked[j] = True
        return True

    #ブロック設置
    def minoDrop(self):
        self.minoDrawing(self.next[0], self.dir)
        self.nextTONext()
        line = self.minoDelete()
        self.score_cal(line)
        self.x = self.initial_x
        self.y = self.initial_y
        self.dir = 0
        if self.DuplicateCheck() == False:
            self.game_over = True
        self.useHold = False
        self.count = 0
    
    #next表示
    def next_draw(self):
        nextField = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for n in range(1,self.next_display+1):
            rect = pygame.Rect(550, (n-1)*105, 96, 96)
            self.screen.fill((self.block_colors[0]), rect)
            for i in range(4):
                for j in range(4):
                    if self.block[self.next[n]][0][i][j] != 0:
                        rect = pygame.Rect(550 + 16*(j+1), (n-1)*105 + 16*(i+1),16,16)
                        self.screen.fill(self.block_colors[self.block[self.next[n]][0][i][j]], rect)

    #hold表示
    def hold_draw(self):
        rect = pygame.Rect(10, 0, 96, 96)
        self.screen.fill((self.block_colors[0]), rect)
        holdField = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for i in range(4):
            for j in range(4):
                if self.block[self.hold][0][i][j] != 0:
                        rect = pygame.Rect(10 + 16*(j+1), 16*(i+1),16,16)
                        self.screen.fill(self.block_colors[self.block[self.hold][0][i][j]], rect)
    def hold_control(self):
        for i in range(4):
            for j in range(4):
                target = self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall]
                if target == self.block[self.next[0]][self.dir][i][j]:
                    self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall] = 0
        if self.hold == 0:
            self.hold = self.next[0]
            self.nextTONext()
        else:
            tmp = self.next[0]
            self.next[0] = self.hold
            self.hold = tmp
        self.x = self.initial_x
        self.y = self.initial_y
        self.dir = 0
        self.hold_draw()
        self.minoDrawing(self.next[0],0)
        self.useHold = True

    #ブロックの回転
    def rotate_block(self, turn):
        for i in range (4):
            for j in range (4):
                target = self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall]
                if target == self.block[self.next[0]][self.dir][i][j]:
                    self.Field[i + self.y + self.Field_top -1][j + self.x + self.Field_wall] = 0
        dirTmp = self.dir
        if turn == 0:#反時計周り
            self.dir -= 1
        elif turn == 1:#時計周り
            self.dir += 1
        if self.dir < 0:
            self.dir = 3
        if self.dir > 3:
            self.dir = 0
        self.useSpin = True
        if self.DuplicateCheck() == False:
            if self.SuperRotation(dirTmp) == False:
                self.dir = dirTmp
        if self.next[0] == 7:
            self.TspinCheck()
        self.minoDrawing(self.next[0], self.dir)
    
    #ライン消去
    def minoDelete(self):
        delete_line = 0
        for i in range(20):
            flag = False
            for j in range(10):
                if self.Field[i + self.Field_top][j + self.Field_wall] == 0:
                    break
                if j == self.Field_width - 1:
                    flag = True
            if flag:
                for j in reversed(range(self.Field_top+1, i + self.Field_top + 1)):
                    for k in range(self.Field_width):
                        self.Field[j][k + self.Field_wall] = self.Field[j-1][k + self.Field_wall]
                        self.Field[j-1][k + self.Field_wall] = 0
                self.line += 1
                delete_line += 1
        return delete_line
                
    #ブロック重複チェック
    def DuplicateCheck(self, srsy = 0, srsx = 0):
        for i in range(4):
            for j in range(4):
                if self.Field[i + self.y + self.Field_top - 1 + srsy][j + self.x + self.Field_wall + srsx] != 0 and self.block[self.next[0]][self.dir][i][j] != 0:
                    return False
        return True

    #スーパーローテーション
    def SuperRotation(self, dirOld):
        movex = 0
        movey = 0
        self.lastSRS = 0
        #I以外
        if self.next[0] != 1:
            if self.dir == 1:
                movex = -1
            elif self.dir == 3:
                movex = 1
            elif self.dir == 0 or self.dir == 2:
                if dirOld == 1:
                    movex = 1
                elif dirOld == 3:
                    movex = -1
            self.lastSRS += 1
            if self.DuplicateCheck(movey, movex) == False:
                if self.dir == 1 or self.dir == 3:
                    movey = -1
                elif self.dir == 0 or self.dir == 2:
                    movey = 1
                self.lastSRS += 1
                if self.DuplicateCheck(movey, movex) == False:
                    movex = 0
                    movey = 0
                    if self.dir == 1 or self.dir == 3:
                        movey = 2
                    elif self.dir == 0 or self.dir == 2:
                        movey = -2
                    self.lastSRS += 1
                    if self.DuplicateCheck(movey, movex) == False:
                        if self.dir == 1:
                            movex = -1
                        elif self.dir == 3:
                            movex = 1
                        elif self.dir == 0 or self.dir == 2:
                            if dirOld == 1:
                                movex = 1
                            elif dirOld == 3:
                                movex = -1
                        self.lastSRS += 1
                        if self.DuplicateCheck(movey, movex) == False:
                            return False
        #I（保留）
        else:
            if self.dir == 1:
                movex = 1
            elif self.dir == 3:
                movex = -1
            elif self.dir == 0 or self.dir == 2:
                if dirOld == 1:
                    movex = -1
                elif dirOld == 3:
                    movex = 1
                if self.dir == 0:
                    movex *= 2
            pt1x = movex
            if self.DuplicateCheck(movey, movex) == False:
                if self.dir == 1:
                    movex = -1
                elif self.dir == 3:
                    movex = 1
                elif self.dir == 0 or self.dir == 2:
                    if dirOld == 1:
                        movex = 1
                    elif dirOld == 3:
                        movex = -1
                    if self.dir == 2:
                        movex *= 2
                pt2x = movex
                if self.DuplicateCheck(movey, movex) == False:
                    if self.dir == 1:
                        movex = pt1x
                        movey = 1
                    elif self.dir == 3:
                        movex = pt1x
                        movey = -1
                    elif self.dir == 0 or self.dir == 2:
                        if dirOld == 1:
                            movex = pt1x
                            movey = -1
                        elif dirOld == 3:
                            movex = pt2x
                            movey = 1
                    if dirOld == 0 and self.dir == 3 or dirOld == 3 and self.dir == 2 or dirOld == 2 and self.dir == 1 or dirOld == 1 and self.dir == 0:
                        movey *= 2
                    if self.DuplicateCheck(movey, movex) == False:
                        if self.dir == 1:
                            movex = pt2x
                            movey = -1
                        elif self.dir == 3:
                            movex = pt2x
                            movey = 1
                        elif self.dir == 0 or self.dir == 2:
                            if dirOld == 1:
                                movex = pt2x
                                movey = 1
                            elif dirOld == 3:
                                movex = pt1x
                                movey = -1
                        if dirOld == 3 and self.dir == 0 or dirOld == 0 and self.dir == 1 or dirOld == 1 and self.dir == 2 or dirOld == 2 and self.dir == 3:
                            movey *= 2
                        if self.DuplicateCheck(movey, movex) == False:
                            return False
        self.x += movex
        self.y += movey
        return True
        
    #Tスピン判定
    def TspinCheck(self):
        tag = 0
        point = [[1,0], [1,2], [3,0], [3,2]]
        around =""
        check_mini = False
        for i in range(4):
            if self.Field[self.y + point[i][0] + self.Field_top - 1][self.x + point[i][1] + self.Field_wall] != 0:
                tag += 1
                sav = 1
            else:
                sav = 0
            around += str(sav)
        #Tspin mini check
        if tag == 3:
            if self.dir == 0:#上
                if around == "1011" or around == "0111":
                    check_mini = True
            if self.dir == 1:#右
                if around == "1110" or around == "1011":
                    check_mini = True
            if self.dir == 2:#下
                if around == "1101" or around == "1110":
                    check_mini = True
            if self.dir == 3:#左
                if around == "0111" or around == "1101":
                    check_mini = True 
        #Tspin check
        if tag >= 3 and self.useSpin:
            self.useTspin = True
            if check_mini and self.lastSRS != 4:
                self.useTspinMini = True
        self.lastSRS = 0

    #スコア表示
    def score_draw(self):
        font = pygame.font.Font(None,50)
        text_score = font.render("Score : " + str(self.score) , True, (255,255,255),0)
        self.screen.blit(text_score, (700, 100))
        text_line = font.render("Line : " + str(self.line) , True, (255,255,255),0)
        self.screen.blit(text_line, (700, 200))
        for i in range(1, numpy.size(self.message)):
            text_message = font.render(str(self.message[i]) , True, (190,20,100),0)
            self.screen.blit(text_message, (700, 400 + 50*i))

    #スコア計算
    def score_cal(self, line):
        self.message = [0]
        point = 0
        btb = False
        #Tspin
        if self.useTspin:
            self.useTspin = False
            self.message.append("T-Spin")
            if line == 0:
                point = 400
            elif line == 1:
                self.message.append("Single")
                point = 800
            elif line == 2:
                self.message.append("Double")
                point = 1200
            elif line == 3:
                self.message.append("Triple")
                point = 1600
            if self.useTspinMini:
                self.useTspinMini = False
                self.message.append("Mini")
                point += 100
            if line != 0:
                btb = True
        #ライン消し
        else:
            if line == 1:
                point = 100
            elif line == 2:
                point = 300
            elif line == 3:
                point = 500
            elif line == 4:
                self.message.append("TETRIS")
                point = 800
                btb = True
            btb = False
        #Back To Back
        if self.BackToBack and btb:
            point = int(point*1.5)
        elif btb == False:
            BackToBack = False
        #REN
        if line > 0:
            if self.ren > 0:
                self.ren += 1
                if self.message == [0]:
                    self.message.append(str(self.ren) + " REN")
            else:
                self.ren += 1
            point += 50 * self.ren
        else:
            self.ren = 0
        #Perfect Clear
        perfect = True
        for i in range(self.Field_hight):
            for j in range(self.Field_width):
                if self.Field[i + self.Field_top][j + self.Field_wall] != 0:
                    perfect = False
        if perfect:
            self.message.append("PERFECT")
            self.message.append("CREAR")
            if line == 1:
                point += 800
            elif line == 2:
                point = 1000
            elif line == 3:
                point = 1800
            elif line == 4:
                point = 2000
        #BTB ならばメッセージ追加
        if self.BackToBack and btb:
            self.message.append("")
            self.message.append("Back To")
            self.message.append("Back")
        #BTB false->true
        if self.BackToBack == False and btb:
            self.BackToBack = True

        
            

    #メインで実行する関数
    def run(self):
        pygame.init()
        pygame.display.set_caption("Test")
        clock = pygame.time.Clock()
        time = 1000
        self.count = 0
        

        while self.game_over == False:
            self.count += 1/time
            self.screen.fill((0,0,0))
            self.nextDecide()
            self.next_draw()
            self.hold_draw()
            self.minoDrawing(self.next[0], self.dir)
            pygame.display.update()
            if(self.count >= 0.5):
                self.free_fall()
                self.count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.minoMoving(3,1)
                    elif event.key == pygame.K_d:
                        self.minoMoving(1,1)
                    elif event.key == pygame.K_s:
                        self.minoMoving(2,1)
                    elif event.key == pygame.K_SPACE:
                        if self.useHold == False:
                            self.hold_control()
                        self.score += 2
                    elif event.key == pygame.K_RIGHT:  # 「→」ボタンを時計回りの回転操作に割り当てる例
                        self.rotate_block(1)
                    elif event.key == pygame.K_LEFT:  # 「←」ボタンを反時計回りの回転操作に割り当てる例
                        self.rotate_block(0)
                    elif event.key == pygame.K_w:
                        #ハードドロップ
                        while(self.MoveCheck(2,1,self.x, self.y, self.dir)):
                            self.minoMoving(2,1)
                            self.score += 2
                        self.minoMoving(2,1)
                        self.score += 2


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            clock.tick(time)
        print(self.score)


# メイン関数
def main():
    tetris_game = Tetris()
    tetris_game.run()

if __name__ == "__main__":
    main()
        

