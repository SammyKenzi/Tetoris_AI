from tetris import Tetris
import pygame
from pygame.locals import *
import random
import numpy
import sys



class Neural_Network(Tetris):
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
        self.game_clear = False
        self.useTspin = False
        self.useTspinMini = False
        self.BackToBack = False
        self.ren = 0
        self.message = ""
        self.best_put = [0,0]
        self.ai_speed = 1
        self.v_delete_line = 0
        #ニューラルネットワークの層
        self.layers = [
            12, #入力層の数
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

    # 1つのニューロンの値を求める関数（入力 x → 次のニューロン）
    def summation(self, x, weights, bias, layer): # x : 外部情報（1次元list）
        neural_sum = 0
        for x_i, w_i in zip(x, weights):
            if numpy.isnan(x_i):
                x_i = 0.0
            neural_sum += int(x_i) * w_i
        return neural_sum
    
    # Relu関数(Output Layer)
    def relu(self, x):
        return numpy.maximum(0,x)
    
    # Mish関数(Middle Layer)
    def mish(self, x):
        softplus = numpy.log(1.0 + numpy.exp(x))
        tanh = (numpy.exp(softplus) - numpy.exp(-softplus)) / (numpy.exp(softplus) + numpy.exp(-softplus))
        return x * tanh

    # 変更
    def minoDrop(self):
        self.minoDrawing(self.next[0], self.dir)
        self.nextTONext()
        line = self.minoDelete(self.Field)
        self.score_cal(line)
        self.x = self.initial_x
        self.y = self.initial_y
        self.dir = 0
        self.best_put = self.learn()
        if self.DuplicateCheck() == False:
            self.game_over = True
        self.useHold = False
        self.count = 0
    
    # 現在のミノを置ける可能性のある場所を羅列する（ミノ設置直後に実行する）
    ### nextの次のやつも見て判断できるようにする
    # →　外部情報の２次元リストを返す
    def next_can_put(self):
        v_x = self.x
        v_y = self.y # 仮想の座標
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
                        v_field[i][j] = self.Field[i][j]
            while(self.MoveCheck(2, 1, v_x, v_y, a, self.Field)):
                v_y += 1
            v_y += 1
            for j in range(4):
                for k in range(4):
                    if self.block[self.next[0]][a][j][k] != 0:
                        v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next[0]
            v_y = 0
            f = self.minoDelete(v_field)
            ###########################################################
            v_x2 = self.x
            v_y2 = self.y # 仮想の座標
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
                while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                    v_y2 += 1
                v_y2 += 1
                for m in range(4):
                    for n in range(4):
                        if self.block[self.next[1]][d][m][n] != 0:
                            v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                v_y2 = 0
                self.v_delete_line = f + self.minoDelete(v_field2)
                # 外部情報を具体的に計算
                info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])

                # v_x2 左方向
                while(self.MoveCheck(3, 1, v_x2, v_y2, d, v_field)):
                    v_x2 -= 1
                    for l in range (24):
                        for m in range (14):
                            v_field2[l][m] = v_field[l][m]
                    while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                    v_y2 = 0
                    self.v_delete_line = f + self.minoDelete(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
            
                # v_x2 右方向
                v_x2 = 3
                count2 = 0
                while(self.MoveCheck(1, 1, v_x2, v_y2, d, v_field)):
                    v_x2 += 1
                    for l in range (24):
                        for m in range (14):
                            v_field2[l][m] = v_field[l][m]
                    while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                    v_y2 = 0
                    self.v_delete_line = f + self.minoDelete(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
            ########################################################

            # v_x 左方向
            while(self.MoveCheck(3, 1, v_x, v_y, a, self.Field)):
                v_x -= 1
                count -= 1
                for i in range (24):
                    for j in range (14):
                        v_field[i][j] = self.Field[i][j]
                while(self.MoveCheck(2, 1, v_x, v_y, a, self.Field)):
                    v_y += 1
                v_y += 1
                for j in range(4):
                    for k in range(4):
                        if self.block[self.next[0]][a][j][k] != 0:
                            v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next[0]
                f = self.minoDelete(v_field)
                v_y = 0
                ###########################################################
                v_x2 = self.x
                v_y2 = self.y # 仮想の座標
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
                    while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                    v_y2 = 0
                    self.v_delete_line = f + self.minoDelete(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
                    
                    # v_x2 左方向
                    while(self.MoveCheck(3, 1, v_x2, v_y2, d, v_field)):
                        v_x2 -= 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                        v_y2 = 0
                        self.v_delete_line = f + self.minoDelete(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
                
                    # v_x2 右方向
                    v_x2 = 3
                    while(self.MoveCheck(1, 1, v_x2, v_y2, d, v_field)):
                        v_x2 += 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                        v_y2 = 0
                        self.v_delete_line = f + self.minoDelete(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
                ########################################################
            # v_x 右方向
            v_x = 3
            v_y = self.y
            count = 0
            while(self.MoveCheck(1, 1, v_x, v_y, a, self.Field)):
                v_x += 1
                count += 1
                for i in range (24):
                    for j in range (14):
                        v_field[i][j] = self.Field[i][j]
                while(self.MoveCheck(2, 1, v_x, v_y, a, self.Field)):
                    v_y += 1
                v_y += 1
                for j in range(4):
                    for k in range(4):
                        if self.block[self.next[0]][a][j][k] != 0:
                            v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next[0]
                v_y = 0
                f = self.minoDelete(v_field)
                ###########################################################
                v_x2 = self.x
                v_y2 = self.y # 仮想の座標
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
                    while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                        v_y2 += 1
                    v_y2 += 1
                    for m in range(4):
                        for n in range(4):
                            if self.block[self.next[1]][d][m][n] != 0:
                                v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                    v_y2 = 0
                    self.v_delete_line = f + self.minoDelete(v_field2)
                    # 外部情報を具体的に計算
                    info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])

                    # v_x2 左方向
                    while(self.MoveCheck(3, 1, v_x2, v_y2, d, v_field)):
                        v_x2 -= 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                        v_y2 = 0
                        self.v_delete_line = f + self.minoDelete(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
                
                    # v_x2 右方向
                    v_x2 = 3
                    while(self.MoveCheck(1, 1, v_x2, v_y2, d, v_field)):
                        v_x2 += 1
                        for l in range (24):
                            for m in range (14):
                                v_field2[l][m] = v_field[l][m]
                        while(self.MoveCheck(2, 1, v_x2, v_y2, d, v_field)):
                            v_y2 += 1
                        v_y2 += 1
                        for m in range(4):
                            for n in range(4):
                                if self.block[self.next[1]][d][m][n] != 0:
                                    v_field2[m + v_y2 + self.Field_top -2][n + v_x2 + self.Field_wall] = self.next[1]
                        v_y2 = 0
                        self.v_delete_line = f + self.minoDelete(v_field2)
                        # 外部情報を具体的に計算
                        info.append([self.cal_input(v_field2, self.Field, self.v_delete_line), a, count])
                ########################################################
        return info

        
    # 外部情報を具体的に計算（1次元配列で返す
    # [高さ、　消せるライン数, 穴の数、穴の上の数]
    '''
    def cal_input(self, field, before_field,line):
        x = []
        #高さ        
        for i in range(24):
            flag = False
            for j in range(2,12):
                if field[i][j] != 0:
                    x.append(i)
                    flag = True
                    break
            if flag:
                break
          
        #消せるライン数
        x.append(line*line*2)
        
        # 穴の数(完全)
        count = 0
        for i in range(22):
            for j in range(2,12):
                if field[i][j] != 0 and field[i+1][j] ==0:
                        count += 1
                    
        x.append(-count)
        
        # 穴の数（部分的）
        count = 0
        for i in range(2,12):
            flag = False
            for j in range(22):
                if field[j][i] != 0:
                    flag = True
                if flag and field[j][i]==0:
                    count += 1
                    
        x.append(-count)

        # 穴の上の数(最高地点のみ)
        sum = 0
        top = []
        top_sum = 0
        for i in range(2,12):
            flag = False
            count = 0
            count_top = 0
            for j in range(22):
                if field[j][i] != 0:
                    if flag == False:
                        top_sum += j
                    flag = True
                    
                if flag:
                    count_top += 1
                if flag and field[j][i]==0:
                    count += 1
                    if count == 1:
                        top.append([count_top-1, j])
            sum += count
        new_top = []
        for i in range(len(top)):
            if top[i][1] == numpy.min(top, axis=0)[1]:
                new_top.append(top[i][0])
        x.append(-sum)
        x.append(top_sum*0.1)
        if new_top == []:
            x.append(0)
        else:
            x.append(-numpy.max(new_top))

        
        # 縦穴
        ## 4マス以上の縦穴が一つなら高評価、二つ以上あるなら低評価  
        count = 0
        for i in range(4,22):
            for j in range(2,12):
                flag = True
                if field[i][j] != 0:
                    if field[i-4][j-1]!=0 and field[i-3][j-1]!=0 and field[i-2][j-1]!=0 and field[i-1][j-1]!=0 and field[i-4][j+1]!=0 and field[i-3][j+1]!=0 and field[i-2][j+1]!=0 and field[i-1][j+1]!=0:
                        k = i-1
                        while k > 0:
                            if field[k][j] != 0:
                                flag = False
                            k -= 1
                if flag:        
                    count += 1
        if count <= 1:
            x.append(0)
        else:
            x.append(0)
        
        
        # 凸凹度
        sa1 = 0
        for i in range(2,11):
            for j in range(24):
                if field[j][i] != 0:
                    left = j
                    break
            for j in range(24):
                if field[j][i+1] != 0:
                    mid = j
                    break
            sa1 += abs(mid - left)
        sa2 = 0
        for i in range(2,11):
            for j in range(24):
                if field[j][i] != 0:
                    left = j
                    break
            for j in range(24):
                if field[j][i+1] != 0:
                    mid = j
                    break
            sa2 += abs(mid - left)
            
        x.append((sa2-sa1)*2)
        x.append((sa2-sa1)*(sa2-sa1)*2)
        
        
        # 一マス空いた行
        flag = True
        gyou = 0
        for i in range(22):
            count = 0
            for j in range(2,12):
                if field[i][j] == 0:
                    count += 1
                    if count > 1:
                        flag = False
                        break
            if flag:
                gyou += 1
        x.append(0)

        # 縦穴のふた（下2マス以上)
        count = 0
        for i in range(22):
            for j in range(2,12):
                if field[i][j] != 0 and field[i+1][j] ==0 and field[i+2][j] == 0:
                        count += 1
                    
        x.append(-count)
        
        return x
    '''
    # Cold Clear を参考にした外部情報（評価値）
    def cal_input(self, field, before_field, line):
        x = []
        # 1: 凸凹度(sa) , 2: 凸凹度の2乗(sasa) , 4: 最高地点の高さ(max_top)
        top = [] # 各列の一番上のブロックの段数
        for i in range(2,12):
            j = 0
            while field[j][i] == 0:
                j += 1
            top.append(j)
        x.append(numpy.min(top))
        sa = 0
        sasa = 0
        for i in range(9):
            sa += abs(top[i] - top[i+1])
            sasa += abs(top[i] - top[i+1]) * abs(top[i] - top[i+1])
        x.append(-sa)
        x.append(-sasa)

        # 3: 各行ごとのブロックの遷移の合計 , 11: オーバーハング (※正確にはオーバーハングではない)(overhang) , 12: オーバーハングの二乗(overhangoverhang)
        count = 0
        overhang = 0
        for i in range(0,22):
            for j in range(2,11):
                if field[i][j] != field[i][j+1]:
                    count += 1
                if field[i][j] != 0 and field[i+1][j] == 0:
                    overhang += 1
        x.append(-count)
        x.append(-overhang)
        overhangoverhang = overhang * overhang
        x.append(-overhangoverhang)

        # 5: 上半分の高さ(sum_top_half)
        sum_top_half = 0 # 上半分の段数の和（小さいほど高評価）
        for i in range(2,12):
            j = 0
            while field[j][i] == 0 and j <=10:
                j += 1
            sum_top_half += 11-j
        x.append(-sum_top_half)

        # 6: 上1/4の高さ(sum_top_quarter)
        sum_top_quarter = 0 # 上半分の段数の和（小さいほど高評価）
        for i in range(2,12):
            j = 0
            while field[j][i] == 0 and j <=5:
                j += 1
            sum_top_quarter += 6-j
        x.append(-sum_top_quarter)

        # 7: 穴の数(cave) , 8: 穴の数の二乗(cavecave) , 9: 穴のセル数(hole) , 10: 穴のセル数の二乗(holehole)
        def count_cavities(board): #[cave, hole]
            def dfs(x, y):
                if 0 <= x < 14 and 0 <= y < 24 and not visited[y][x] and not board[y][x]:
                    visited[y][x] = True
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        dfs(nx, ny)

            def count_connected_zeros(x, y):
                if not (0 <= x < 14 and 0 <= y < 24) or visited[y][x] or board[y][x] != 0:
                    return 0
                visited[y][x] = True
                count = 1
                count += count_connected_zeros(x + 1, y)
                count += count_connected_zeros(x - 1, y)
                count += count_connected_zeros(x, y + 1)
                count += count_connected_zeros(x, y - 1)
                return count
            def count_connected_zeros_top(board):
                    def dfs2(x, y):
                        if not (0 <= x < 14 and 0 <= y < 24) or visited[y][x] or board[y][x] != 0:
                            return 0
                        visited[y][x] = True
                        count = 1
                        count += dfs2(x + 1, y)
                        count += dfs2(x - 1, y)
                        count += dfs2(x, y + 1)
                        count += dfs2(x, y - 1)
                        return count
                    visited = [[False] * 14 for _ in range(24)]
                    return dfs2(2, 0)
            visited = [[False for _ in range(14)] for _ in range(24)]
            cavity_count = 0
            cell_count = 0

            for y in range(24):
                for x in range(14):
                    if not visited[y][x] and not board[y][x]:
                        cavity_count += 1
                        cell_count += count_connected_zeros(x, y)
                        dfs(x, y)

            return cavity_count-1, cell_count-count_connected_zeros_top(board)
        cave_hole = count_cavities(field)
        cave = cave_hole[0]
        cavecave = cave_hole[0] * cave_hole[0]
        hole = cave_hole[1]
        holehole = cave_hole[1] * cave_hole[1]
        x.append(-cave)
        x.append(-cavecave)
        x.append(-hole)
        x.append(-holehole)


        return x



    def play_ai(self):
        move_count = 0
        if self.dir != self.best_put[0]:
                if self.best_put[0] == 1:
                    self.rotate_block(1)
                elif self.best_put[0] == 2:
                    self.rotate_block(1)
                    self.rotate_block(1)
                elif self.best_put[0] == 3:
                    self.rotate_block(0)
        while move_count != self.best_put[1]:
            if self.best_put[1] > 0:
                self.minoMoving(1,1)
                move_count += 1
            else:
                self.minoMoving(3,1)
                move_count -= 1
        while(self.MoveCheck(2,1,self.x, self.y, self.dir, self.Field)):
            self.minoMoving(2,1)
            #self.score += 2
        self.minoMoving(2,1)
        #self.score += 2
    
    # 出力層の値の最大値とその時の情報を返す関数[dir, 座標]
    def learn(self):
        # 外部情報のlist x(2次元)　を取得
        x = self.next_can_put()
        output = []
        for k in range(len(x)):
            # 入力層→中間層
            middle_x = []
            for i in range(self.layers[1]):
                middle_x.append(self.summation(x[k][0], self.weights[0][i], self.biases[0][i], 1))
            # 中間層→出力層
            output.append([self.summation(middle_x, self.weights[1][0], self.biases[1][0],2), x[k][1], x[k][2]])
        max_index = numpy.argmax(numpy.array(output), axis=0).tolist()
        return [output[max_index[0]][1], output[max_index[0]][2]]


    def run(self, p1, p2):
        pygame.init()
        pygame.display.set_caption("AI")
        clock = pygame.time.Clock()
        time = 1000
        self.count = 0
        self.weights = p1
        self.biases = p2

        while self.game_over == False and self.game_clear == False:
            if self.line >= 40:
                self.game_clear = True
            self.count += 1/time
            self.screen.fill((0,0,0))
            self.nextDecide()
            self.next_draw()
            self.hold_draw()
            self.minoDrawing(self.next[0], self.dir)
            pygame.display.update()

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

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            clock.tick(time)
        if self.game_over:
            self.score = -1000
        print(self.score)
        return self.score




# メイン関数
def main():
    for i in range(2):
        neural = Neural_Network()
        neural.run([0.5687704444210947, 0.7514973650297183, 0.5999409274909423, 0.3160275218886778, 0.5649244889410366, 0.056615117677696336, 0.8049260401867924, 0.2135799446852602, 0.9232150419431141, 0.8805907136485752, 0.21958168475209816, 0.39345737845541406, 0.4143307471447828, 0.37777281617494574, 0.8568384085120957, 0.8788756418422684, 0.9130737355988718, 0.32779641878412835, 0.08852187739344652, 0.49554531080780306, 0.4537544189441871, 0.2588918321184205, 0.018643081348969193, 0.20213123684666912, 0.49600564548643544, 0.28553855718433707, 0.6838658241374191, 0.5746408897812404]
            )

if __name__ == "__main__":
    main()