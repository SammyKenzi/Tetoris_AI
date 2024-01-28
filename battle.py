from neural_network import Neural_Network
import pygame
from pygame.locals import *
import random
import numpy
import sys

class Battle(Neural_Network):
    def __init__(self):
        self.Field_width = 10
        self.Field_hight = 20
        self.Field_wall = 2
        self.Field_top = 2
        self.screen = pygame.display.set_mode((1800, 660))
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
        self.Field2 = [[8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
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
        #player1
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
        self.game_clear = False
        self.useTspin = False
        self.useTspinMini = False
        self.BackToBack = False
        self.ren = 0
        self.message = ""
        self.best_put = [0,0]
        self.ai_speed = 100
        self.v_delete_line = 0
        self.attacked = 0
        #player2
        self.initial_x2 = 3
        self.initial_y2 = 0
        self.x2 = self.initial_x2
        self.y2 = self.initial_y2
        self.next2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.tonextCount2 = 0
        self.dir2 = 0
        self.next_display2 = 6
        self.score2 = 0
        self.line2 = 0
        self.hold2 = 0
        self.useHold2 = False
        self.ghostY2 = 0
        self.count2 = 0
        self.game_over2 = False
        self.game_clear2 = False
        self.useTspin2 = False
        self.useTspinMini2 = False
        self.BackToBack2 = False
        self.ren2 = 0
        self.message2 = ""
        self.best_put2 = [0,0]
        self.ai_speed2 = 0
        self.v_delete_line2 = 0
        self.attacked2 = 0
        #ニューラルネットワークの層
        self.layers = [
            7, #入力層の数
            3, #中間層の数
            1] #出力層の数
        
        #重みとバイアスの初期値
        self.weights = [
            [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], # 入力層→中間層1　入力層→中間層2　入力層→中間層3
            [[0.0, 0.0, 0.0]] # 中間層→出力層
        ]
        self.biases = [
            [0.0, 0.0, 0.0], # 中間層のバイアス
            [0.0] # 出力層のバイアス
        ]
        self.weights2 = self.weights
        self.biases2 = self.biases
    
    # Player2
    #nextをランダムに決める
    def nextDecide2(self):
        val = [7,1,2,3,4,5,6]
        loop = int(numpy.size(self.next2) / 7)
        for i in range (loop):
            if self.next2[i * 7] == 0:
                random.shuffle(val)
                for j in range (7):
                    self.next2[i * 7 + j] = val[j]

    #nextを更新
    def nextTONext2(self):
        for i in range (numpy.size(self.next2)-1):
            self.next2[i] = self.next2[i+1]
        self.next2[numpy.size(self.next2)-1] = 0
        self.tonextCount2 += 1
        if self.tonextCount2 == 7:
            self.nextDecide2()
            self.tonextCount2 = 0

    #方向と距離を引数とした、ブロックの移動
    def minoMoving2(self, move, pwr):
        for i in range (4):
            for j in range (4):
                target = self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall]
                if target == self.block[self.next2[0]][self.dir2][i][j]:
                    self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall] = 0
        if self.MoveCheck2(move, pwr, self.x2, self.y2, self.dir2,self.Field2):
            if move == 0:
                self.y2 += -pwr
            elif move == 1:
                self.x2 += pwr
            elif move == 2:
                self.y2 += pwr
            elif move == 3:
                self.x2 += -pwr
            self.useSpin2 = False
            self.minoDrawing2(self.next2[0], self.dir2)
        elif move == 2:
            self.minoDrop2()

    #自由落下
    def free_fall2(self):
        self.minoMoving2(2,1)

    #描画
    def draw(self):
        ## Player1
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
        ## Player2
        #mino
        for i in range (2,24):
            for j in range (14):
                rect = pygame.Rect(900+120+30*j,30*(i - self.Field_top),30,30)
                self.screen.fill(self.block_colors[self.Field2[i][j]], rect)
        #ghost
        for i in range (4):
            for j in range (4):
                if self.block[self.next2[0]][self.dir2][i][j] != 0:
                    rect = pygame.Rect(900+180+30*(self.x2+j),30*(self.ghost2()+i)-30,30,30)
                    self.screen.fill(self.block_colors[10* self.next2[0]], rect)
        #line
        for i in range(9):
            pygame.draw.line(self.screen, (200,200,200), (900+210+30*i, 0), (900+210+30*i, 600), 1)
        for i in range(19):
            pygame.draw.line(self.screen, (200,200,200), (900+180, i*30 + 30), (900+480, i*30 + 30), 1)
        #Score
        self.score_draw()
        # Attack
        self.attack_draw()

    #Ghost表示
    def ghost2(self):
        self.ghostY2 = 0
        while(self.MoveCheck2(2,1,self.x2, self.y2, self.dir2, self.Field2, 0,self.ghostY2)):
            self.ghostY2 += 1
        return self.ghostY2 + self.y2

    #ブロックの位置情報を更新して描画
    def minoDrawing2(self, m, d):
        for i in range(4):
            for j in range(4):
                if self.block[m][d][i][j] != 0:
                    self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall] = self.block[m][d][i][j]
        self.draw()
    
    #衝突判定
    def MoveCheck2(self, direction, power, self_x, self_y, dir, field, srsx=0, srsy=0 ):
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
                if self.block[self.next2[0]][dir][diry][dirx] != 0:
                    if direction == 0:
                        if field[diry + self_y - power + self.Field_top - 1 + srsy][dirx + self_x + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    elif direction == 1:
                        if field[diry + self_y + self.Field_top - 1 + srsy][dirx + self_x + power + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    elif direction == 2:
                        if field[diry + self_y + power + self.Field_top - 1 + srsy][dirx + self_x + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    elif direction == 3:
                        if field[diry + self_y + self.Field_top - 1 + srsy][dirx + self_x - power + self.Field_wall + srsx] != 0 and checked[j] != True:
                            return False
                    checked[j] = True
        return True

    
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
        nextField = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for n in range(1,self.next_display2+1):
            rect = pygame.Rect(900+550, (n-1)*105, 96, 96)
            self.screen.fill((self.block_colors[0]), rect)
            for i in range(4):
                for j in range(4):
                    if self.block[self.next2[n]][0][i][j] != 0:
                        rect = pygame.Rect(900+550 + 16*(j+1), (n-1)*105 + 16*(i+1),16,16)
                        self.screen.fill(self.block_colors[self.block[self.next2[n]][0][i][j]], rect)
    '''
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
        rect = pygame.Rect(10, 0, 96, 96)
        self.screen.fill((self.block_colors[0]), rect)
        holdField = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for i in range(4):
            for j in range(4):
                if self.block[self.hold2][0][i][j] != 0:
                        rect = pygame.Rect(900+10 + 16*(j+1), 16*(i+1),16,16)
                        self.screen.fill(self.block_colors[self.block[self.hold2][0][i][j]], rect)
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
        for i in range(4):
            for j in range(4):
                target = self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall]
                if target == self.block[self.next2[0]][self.dir2][i][j]:
                    self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall] = 0
        if self.hold2 == 0:
            self.hold2 = self.next2[0]
            self.nextTONext2()
        else:
            tmp = self.next2[0]
            self.next2[0] = self.hold2
            self.hold2 = tmp
        self.x2 = self.initial_x2
        self.y2 = self.initial_y2
        self.dir2 = 0
        self.hold_draw()
        self.minoDrawing2(self.next2[0],0)
        self.useHold = True
    '''
    #ブロックの回転
    def rotate_block2(self, turn):
        for i in range (4):
            for j in range (4):
                target = self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall]
                if target == self.block[self.next2[0]][self.dir2][i][j]:
                    self.Field2[i + self.y2 + self.Field_top -1][j + self.x2 + self.Field_wall] = 0
        dirTmp = self.dir2
        if turn == 0:#反時計周り
            self.dir2 -= 1
        elif turn == 1:#時計周り
            self.dir2 += 1
        if self.dir2 < 0:
            self.dir2 = 3
        if self.dir2 > 3:
            self.dir2 = 0
        self.useSpin2 = True
        if self.DuplicateCheck2() == False:
            if self.SuperRotation2(dirTmp) == False:
                self.dir2 = dirTmp
        if self.next2[0] == 7:
            self.TspinCheck2()
        self.minoDrawing2(self.next2[0], self.dir2)
    
    #ライン消去1
    def minoDelete(self, field):
        delete_line = 0
        v_delete_line = 0
        for i in range(20):
            flag = False
            for j in range(10):
                if field[i + self.Field_top][j + self.Field_wall] == 0:
                    break
                if j == self.Field_width - 1:
                    flag = True
            if flag:
                for j in reversed(range(self.Field_top+1, i + self.Field_top + 1)):
                    for k in range(self.Field_width):
                        field[j][k + self.Field_wall] = field[j-1][k + self.Field_wall]
                        field[j-1][k + self.Field_wall] = 0
                if field == self.Field:
                    self.line += 1
                    delete_line += 1
                else:
                    v_delete_line += 1
        if field == self.Field:
            self.score += delete_line * delete_line
            self.attacked2 += delete_line
            return delete_line
        else:
            return v_delete_line

    #ライン消去2
    def minoDelete2(self, field):
        delete_line = 0
        v_delete_line = 0
        for i in range(20):
            flag = False
            for j in range(10):
                if field[i + self.Field_top][j + self.Field_wall] == 0:
                    break
                if j == self.Field_width - 1:
                    flag = True
            if flag:
                for j in reversed(range(self.Field_top+1, i + self.Field_top + 1)):
                    for k in range(self.Field_width):
                        field[j][k + self.Field_wall] = field[j-1][k + self.Field_wall]
                        field[j-1][k + self.Field_wall] = 0
                if field == self.Field2:
                    self.line2 += 1
                    delete_line += 1
                else:
                    v_delete_line += 1
        if field == self.Field2:
            self.score2 += delete_line * delete_line
            self.attacked += delete_line
            return delete_line
        else:
            return v_delete_line

    def minoDrop(self):
        self.minoDrawing(self.next[0], self.dir)
        self.nextTONext()
        line = self.minoDelete(self.Field)
        self.score_cal(line)
        self.x = self.initial_x
        self.y = self.initial_y
        self.dir = 0
        self.do_attack(self.attacked2)
        self.attacked2 = 0
        self.best_put = self.learn()
        if self.DuplicateCheck() == False:
            self.game_over = True
        self.useHold = False
        self.count = 0        
    def minoDrop2(self):
        self.minoDrawing2(self.next2[0], self.dir2)
        self.nextTONext2()
        line = self.minoDelete2(self.Field2)
        self.score_cal(line)
        self.x2 = self.initial_x2
        self.y2 = self.initial_y2
        self.dir2 = 0
        self.do_attack2(self.attacked)
        self.attacked = 0
        self.best_put2 = self.learn2()
        if self.DuplicateCheck2() == False:
            self.game_over2 = True
        self.useHold2 = False
        self.count2 = 0        
                
    #ブロック重複チェック
    def DuplicateCheck2(self, srsy = 0, srsx = 0):
        flag = True
        for i in range(4):
            for j in range(4):
                if self.Field2[i + self.y2 + self.Field_top - 1 + srsy][j + self.x2 + self.Field_wall + srsx] != 0 and self.block[self.next2[0]][self.dir2][i][j] != 0:
                    flag = False
        return flag

    #スーパーローテーション
    def SuperRotation2(self, dirOld):
        movex = 0
        movey = 0
        self.lastSRS2 = 0
        #I以外
        if self.next2[0] != 1:
            if self.dir2 == 1:
                movex = -1
            elif self.dir2 == 3:
                movex = 1
            elif self.dir2 == 0 or self.dir2 == 2:
                if dirOld == 1:
                    movex = 1
                elif dirOld == 3:
                    movex = -1
            self.lastSRS2 += 1
            if self.DuplicateCheck2(movey, movex) == False:
                if self.dir2 == 1 or self.dir2 == 3:
                    movey = -1
                elif self.dir2 == 0 or self.dir2 == 2:
                    movey = 1
                self.lastSRS2 += 1
                if self.DuplicateCheck2(movey, movex) == False:
                    movex = 0
                    movey = 0
                    if self.dir2 == 1 or self.dir2 == 3:
                        movey = 2
                    elif self.dir2 == 0 or self.dir2 == 2:
                        movey = -2
                    self.lastSRS2 += 1
                    if self.DuplicateCheck2(movey, movex) == False:
                        if self.dir2 == 1:
                            movex = -1
                        elif self.dir2 == 3:
                            movex = 1
                        elif self.dir2 == 0 or self.dir2 == 2:
                            if dirOld == 1:
                                movex = 1
                            elif dirOld == 3:
                                movex = -1
                        self.lastSRS2 += 1
                        if self.DuplicateCheck2(movey, movex) == False:
                            return False
        #I（保留）
        else:
            if self.dir2 == 1:
                movex = 1
            elif self.dir2 == 3:
                movex = -1
            elif self.dir2 == 0 or self.dir2 == 2:
                if dirOld == 1:
                    movex = -1
                elif dirOld == 3:
                    movex = 1
                if self.dir2 == 0:
                    movex *= 2
            pt1x = movex
            if self.DuplicateCheck2(movey, movex) == False:
                if self.dir2 == 1:
                    movex = -1
                elif self.dir2 == 3:
                    movex = 1
                elif self.dir2 == 0 or self.dir2 == 2:
                    if dirOld == 1:
                        movex = 1
                    elif dirOld == 3:
                        movex = -1
                    if self.dir2 == 2:
                        movex *= 2
                pt2x = movex
                if self.DuplicateCheck2(movey, movex) == False:
                    if self.dir2 == 1:
                        movex = pt1x
                        movey = 1
                    elif self.dir2 == 3:
                        movex = pt1x
                        movey = -1
                    elif self.dir2 == 0 or self.dir2 == 2:
                        if dirOld == 1:
                            movex = pt1x
                            movey = -1
                        elif dirOld == 3:
                            movex = pt2x
                            movey = 1
                    if dirOld == 0 and self.dir2 == 3 or dirOld == 3 and self.dir2 == 2 or dirOld == 2 and self.dir2 == 1 or dirOld == 1 and self.dir2 == 0:
                        movey *= 2
                    if self.DuplicateCheck2(movey, movex) == False:
                        if self.dir2 == 1:
                            movex = pt2x
                            movey = -1
                        elif self.dir2 == 3:
                            movex = pt2x
                            movey = 1
                        elif self.dir2 == 0 or self.dir2 == 2:
                            if dirOld == 1:
                                movex = pt2x
                                movey = 1
                            elif dirOld == 3:
                                movex = pt1x
                                movey = -1
                        if dirOld == 3 and self.dir2 == 0 or dirOld == 0 and self.dir2 == 1 or dirOld == 1 and self.dir2 == 2 or dirOld == 2 and self.dir2 == 3:
                            movey *= 2
                        if self.DuplicateCheck2(movey, movex) == False:
                            return False
        self.x2 += movex
        self.y2 += movey
        return True
        
    #Tスピン判定
    def TspinCheck2(self):
        tag = 0
        point = [[1,0], [1,2], [3,0], [3,2]]
        around =""
        check_mini = False
        for i in range(4):
            if self.Field2[self.y2 + point[i][0] + self.Field_top - 1][self.x2 + point[i][1] + self.Field_wall] != 0:
                tag += 1
                sav = 1
            else:
                sav = 0
            around += str(sav)
        #Tspin mini check
        if tag == 3:
            if self.dir2 == 0:#上
                if around == "1011" or around == "0111":
                    check_mini = True
            if self.dir2 == 1:#右
                if around == "1110" or around == "1011":
                    check_mini = True
            if self.dir2 == 2:#下
                if around == "1101" or around == "1110":
                    check_mini = True
            if self.dir2 == 3:#左
                if around == "0111" or around == "1101":
                    check_mini = True 
        #Tspin check
        if tag >= 3 and self.useSpin2:
            self.useTspin2 = True
            if check_mini and self.lastSRS2 != 4:
                self.useTspinMini2 = True
        self.lastSRS2 = 0

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
        font = pygame.font.Font(None,50)
        text_score = font.render("Score : " + str(self.score2) , True, (255,255,255),0)
        self.screen.blit(text_score, (900+700, 100))
        text_line = font.render("Line : " + str(self.line2) , True, (255,255,255),0)
        self.screen.blit(text_line, (900+700, 200))
        for i in range(1, numpy.size(self.message2)):
            text_message = font.render(str(self.message2[i]) , True, (190,20,100),0)
            self.screen.blit(text_message, (900+700, 400 + 50*i))

    #スコア計算
    def score_cal2(self, line):
        self.message2 = [0]
        point = 0
        btb = False
        #Tspin
        if self.useTspin2:
            self.useTspin2 = False
            self.message2.append("T-Spin")
            if line == 0:
                point = 400
            elif line == 1:
                self.message2.append("Single")
                point = 800
            elif line == 2:
                self.message2.append("Double")
                point = 1200
            elif line == 3:
                self.message2.append("Triple")
                point = 1600
            if self.useTspinMini2:
                self.useTspinMini2 = False
                self.message2.append("Mini")
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
                self.message2.append("TETRIS")
                point = 800
                btb = True
            btb = False
        #Back To Back
        if self.BackToBack2 and btb:
            point = int(point*1.5)
        elif btb == False:
            BackToBack = False
        #REN
        if line > 0:
            if self.ren2 > 0:
                self.ren2 += 1
                if self.message2 == [0]:
                    self.message2.append(str(self.ren2) + " REN")
            else:
                self.ren2 += 1
            point += 50 * self.ren2
        else:
            self.ren2 = 0
        #Perfect Clear
        perfect = True
        for i in range(self.Field_hight):
            for j in range(self.Field_width):
                if self.Field2[i + self.Field_top][j + self.Field_wall] != 0:
                    perfect = False
        if perfect:
            self.message2.append("PERFECT")
            self.message2.append("CREAR")
            if line == 1:
                point += 800
            elif line == 2:
                point = 1000
            elif line == 3:
                point = 1800
            elif line == 4:
                point = 2000
        #BTB ならばメッセージ追加
        if self.BackToBack2 and btb:
            self.message2.append("")
            self.message2.append("Back To")
            self.message2.append("Back")
        #BTB false->true
        if self.BackToBack2 == False and btb:
            self.BackToBack2 = True

    # 攻撃表示
    def attack_draw(self):
        font = pygame.font.Font(None,50)
        text_num = font.render(" x " + str(self.attacked), True, (255,255,255),0)
        self.screen.blit(text_num, (700,610))
        rect = pygame.Rect(650, 600, 40, 40)
        self.screen.fill((self.block_colors[8]), rect)
        font = pygame.font.Font(None,50)
        text_num = font.render(" x " + str(self.attacked2), True, (255,255,255),0)
        self.screen.blit(text_num, (900+700,610))
        rect = pygame.Rect(900+650, 600, 40, 40)
        self.screen.fill((self.block_colors[8]), rect)

    # 攻撃実行
    def do_attack(self, pwr):
        flag = False
        for i in range(3,22):
            for j in range(2,12):
                if i < 22-pwr:
                    self.Field2[i][j] = self.Field2[i+pwr][j]
                else:
                    flag = True
                    self.Field2[i][j] = 9
            if flag:
                x = random.randint(2,11)
                self.Field2[i][x] = 0

    def do_attack2(self, pwr):
        flag = False
        for i in range(3,22):
            for j in range(2,12):
                if i < 22-pwr:
                    self.Field[i][j] = self.Field[i+pwr][j]
                else:
                    flag = True
                    self.Field[i][j] = 9
            if flag:
                x = random.randint(2,11)
                self.Field[i][x] = 0


    def next_can_put2(self):
        v_x = self.x2
        v_y = self.y2 # 仮想の座標
        info = []
        for a in range(4):
            count = 0
            v_field = [[8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
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
            
            v_x = 3
            # v_x 初期値
            for i in range (24):
                    for j in range (14):
                        v_field[i][j] = self.Field2[i][j]
            while(self.MoveCheck2(2, 1, v_x, v_y, a, self.Field2)):
                v_y += 1
            v_y += 1
            for j in range(4):
                for k in range(4):
                    if self.block[self.next2[0]][a][j][k] != 0:
                        v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next2[0]
            v_y = 0
            f = self.minoDelete2(v_field)
            ###########################################################
            v_x2 = self.x2
            v_y2 = self.y2 # 仮想の座標
            for d in range(4):
                v_field2 = [[8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
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
            
                v_x2 = 3
                # v_x2 初期値
                for l in range (24):
                        for m in range (14):
                            v_field2[l][m] = v_field[l][m]
                while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                    v_y2 += 1
                v_y2 += 1
                for m in range(4):
                    for n in range(4):
                        if self.block[self.next2[1]][d][m][n] != 0:
                            v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                v_y2 = 0
                self.v_delete_line2 = f + self.minoDelete2(v_field2)
                # 外部情報を具体的に計算
                info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])

                # v_x2 左方向
                while(self.MoveCheck2(3, 1, v_x2, v_y2, d, v_field)):
                    v_x2 -= 1
                    for l in range (24):
                        for m in range (14):
                            v_field2[l][m] = v_field[l][m]
                    while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next2[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                    v_y2 = 0
                    self.v_delete_line2 = f + self.minoDelete2(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
            
                # v_x2 右方向
                v_x2 = 3
                count2 = 0
                while(self.MoveCheck2(1, 1, v_x2, v_y2, d, v_field)):
                    v_x2 += 1
                    for l in range (24):
                        for m in range (14):
                            v_field2[l][m] = v_field[l][m]
                    while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next2[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                    v_y2 = 0
                    self.v_delete_line2 = f + self.minoDelete2(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
            ########################################################

            # v_x 左方向
            while(self.MoveCheck2(3, 1, v_x, v_y, a, self.Field2)):
                v_x -= 1
                count -= 1
                for i in range (24):
                    for j in range (14):
                        v_field[i][j] = self.Field2[i][j]
                while(self.MoveCheck2(2, 1, v_x, v_y, a, self.Field2)):
                    v_y += 1
                v_y += 1
                for j in range(4):
                    for k in range(4):
                        if self.block[self.next2[0]][a][j][k] != 0:
                            v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next2[0]
                f = self.minoDelete2(v_field)
                v_y = 0
                ###########################################################
                v_x2 = self.x2
                v_y2 = self.y2 # 仮想の座標
                for d in range(4):
                    v_field2 = [[8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
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
                
                    v_x2 = 3
                    # v_x2 初期値
                    for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                    while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next2[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                    v_y2 = 0
                    self.v_delete_line2 = f + self.minoDelete2(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
                    
                    # v_x2 左方向
                    while(self.MoveCheck2(3, 1, v_x2, v_y2, d, v_field)):
                        v_x2 -= 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next2[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                        v_y2 = 0
                        self.v_delete_line2 = f + self.minoDelete2(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
                
                    # v_x2 右方向
                    v_x2 = 3
                    while(self.MoveCheck2(1, 1, v_x2, v_y2, d, v_field)):
                        v_x2 += 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next2[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                        v_y2 = 0
                        self.v_delete_line2 = f + self.minoDelete2(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
                ########################################################
            # v_x 右方向
            v_x = 3
            v_y = self.y2
            count = 0
            while(self.MoveCheck2(1, 1, v_x, v_y, a, self.Field2)):
                v_x += 1
                count += 1
                for i in range (24):
                    for j in range (14):
                        v_field[i][j] = self.Field2[i][j]
                while(self.MoveCheck2(2, 1, v_x, v_y, a, self.Field2)):
                    v_y += 1
                v_y += 1
                for j in range(4):
                    for k in range(4):
                        if self.block[self.next2[0]][a][j][k] != 0:
                            v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next2[0]
                v_y = 0
                f = self.minoDelete2(v_field)
                ###########################################################
                v_x2 = self.x2
                v_y2 = self.y2 # 仮想の座標
                for d in range(4):
                    v_field2 = [[8,8, 0,0,0,0,0,0,0,0,0,0, 8,8],
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
                
                    v_x2 = 3
                    # v_x2 初期値
                    for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                    while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next2[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                    v_y2 = 0
                    self.v_delete_line2 = f + self.minoDelete2(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])

                    # v_x2 左方向
                    while(self.MoveCheck2(3, 1, v_x2, v_y2, d, v_field)):
                        v_x2 -= 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next2[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                        v_y2 = 0
                        self.v_delete_line2 = f + self.minoDelete2(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
                
                    # v_x2 右方向
                    v_x2 = 3
                    while(self.MoveCheck2(1, 1, v_x2, v_y2, d, v_field)):
                        v_x2 += 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck2(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next2[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next2[1]
                        v_y2 = 0
                        self.v_delete_line2 = f + self.minoDelete2(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field2, self.v_delete_line2), a, count])
                ########################################################
        return info

    # 出力層の値の最大値とその時の情報を返す関数[dir, 座標]
    def learn2(self):
        # 外部情報のlist x(2次元)　を取得
        x = self.next_can_put2()
        output = []
        for k in range(len(x)):
            # 入力層→中間層
            middle_x = []
            for i in range(self.layers[1]):
                middle_x.append(self.summation(x[k][0], self.weights2[0][i], self.biases2[0][i], 1))
            # 中間層→出力層
            output.append([self.summation(middle_x, self.weights2[1][0], self.biases2[1][0],2), x[k][1], x[k][2]])
        max_index = numpy.argmax(numpy.array(output), axis=0).tolist()
        return [output[max_index[0]][1], output[max_index[0]][2]]

    def play_ai2(self):
        move_count = 0
        if self.dir2 != self.best_put2[0]:
                if self.best_put2[0] == 1:
                    self.rotate_block2(1)
                elif self.best_put2[0] == 2:
                    self.rotate_block2(1)
                    self.rotate_block2(1)
                elif self.best_put2[0] == 3:
                    self.rotate_block2(0)
        while move_count != self.best_put2[1]:
            if self.best_put2[1] > 0:
                self.minoMoving2(1,1)
                move_count += 1
            else:
                self.minoMoving2(3,1)
                move_count -= 1
        while(self.MoveCheck2(2,1,self.x2, self.y2, self.dir2, self.Field2)):
            self.minoMoving2(2,1)
            #self.score += 2
        self.minoMoving2(2,1)
        #self.score += 2

    def run(self,p1,p2):
        pygame.init()
        pygame.display.set_caption("AI")
        clock = pygame.time.Clock()
        time = 1000
        self.count = 0
        self.weights = p1
        self.biases = p2
        self.weights2 = p1
        self.biases2 = p2

        while self.game_over == False and self.game_over2 == False:
            #if self.line >= 40:
            #    self.game_clear = True
            self.screen.fill((0,0,0))
            self.nextDecide()
            self.minoDrawing(self.next[0], self.dir)
            self.nextDecide2()
            self.minoDrawing2(self.next2[0], self.dir2)
            self.next_draw()
            pygame.display.update()

            # Player1
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
                    #elif event.key == pygame.K_SPACE:
                    #    if self.useHold == False:
                    #        self.hold_control()
                        #self.score += 2
                    elif event.key == pygame.K_RIGHT:  # 「→」ボタンを時計回りの回転操作に割り当てる例
                        self.rotate_block(1)
                    elif event.key == pygame.K_LEFT:  # 「←」ボタンを反時計回りの回転操作に割り当てる例
                        self.rotate_block(0)
                    elif event.key == pygame.K_w:
                        #ハードドロップ
                        while(self.MoveCheck(2,1,self.x, self.y, self.dir, self.Field)):
                            self.minoMoving(2,1)
                            #self.score += 2
                        self.minoMoving(2,1)
                        #self.score += 2
            
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
                        #self.score += 2
                    elif event.key == pygame.K_RIGHT:  # 「→」ボタンを時計回りの回転操作に割り当てる例
                        self.rotate_block(1)
                    elif event.key == pygame.K_LEFT:  # 「←」ボタンを反時計回りの回転操作に割り当てる例
                        self.rotate_block(0)
                    elif event.key == pygame.K_w:
                        #ハードドロップ
                        while(self.MoveCheck(2,1,self.x, self.y, self.dir, self.Field)):
                            self.minoMoving(2,1)
                            #self.score += 2
                        self.minoMoving(2,1)
                        #self.score += 2


            # Played by AI
            self.play_ai()
            self.play_ai2()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            clock.tick(time)
        if self.game_over:
            winner = 2
        else:
            winner = 1
        print(winner)
        return winner

def main():
    battle = Battle()
    battle.run([[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],[[0.0, 0.0, 0.0]]],[[0.0, 0.0, 0.0],[0.0]])

if __name__ == "__main__":
    main()