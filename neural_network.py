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
        self.useTspin = False
        self.useTspinMini = False
        self.BackToBack = False
        self.ren = 0
        self.message = ""
        #ニューラルネットワークの層
        self.layers = [
            2, #入力層の数
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
    def summation(self, x, weights, bias): # x : 外部情報（1次元list）
        neural_sum = 0
        for x_i, w_i in zip(x, weights):
            neural_sum += int(x_i) * w_i
        neural_sum += bias
        return neural_sum

    # 変更
    def minoDrop(self):
        self.minoDrawing(self.next[0], self.dir)
        self.nextTONext()
        line = self.minoDelete()
        self.score_cal(line)
        self.x = self.initial_x
        self.y = self.initial_y
        self.dir = 0
        self.learn()
        if self.DuplicateCheck() == False:
            self.game_over = True
        self.useHold = False
        self.count = 0
    


    
    # 現在のミノを置ける可能性のある場所を羅列する（ミノ設置直後に実行する）
    # →　外部情報の２次元リストを返す
    def next_can_put(self):
        v_x = self.x
        v_y = self.y # 仮想の座標
        info = []
        for a in range(4):
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
            for i in range (24):
                for j in range (14):
                    v_field[i][j] = self.Field[i][j]
            while(self.MoveCheck(3, 1, v_x, v_y, self.next[0])):
                v_x -= 1
            
            while(self.MoveCheck(2, 1, v_x, v_y, self.next[0])):
                v_y += 1
            for j in range(4):
                for k in range(4):
                    if self.block[self.next[0]][a][j][k] != 0:
                        v_field[j + v_y + self.Field_top -2][k + v_x + self.Field_wall] = self.next[0]
            # 外部情報を具体的に計算
            info.append(self.cal_input(v_field))
        return info

        
    # 外部情報を具体的に計算（1次元配列で返す
    # [低さ、　消せるライン数]
    def cal_input(self, field):
        #低さ（低いほうがいい）
        x = []
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
        line = 0
        for i in range(22):
            flag = True
            for j in range(2,12):
                if field[i][j] == 0:
                    flag = False
                    break
            if flag:
                line += 1
        x.append(line)
        return x
    
    # 出力層の値の最大値とその時の情報を返す関数[最大値, 外部情報の何番目か]
    def learn(self):
        # 外部情報のlist x(2次元)　を取得
        x = self.next_can_put()
        output = []
        for k in range(len(x)):
            # 入力層→中間層
            middle_x = []
            for i in range(self.layers[1]):
                middle_x.append(self.summation(x[k], self.weights[0][i], self.biases[0][i]))
            # 中間層→出力層
            output.append(self.summation(middle_x, self.weights[1][0], self.biases[1][0]))
        max_value = max(output)
        return [max_value, output.index(max_value)]
    
    def run(self):
        pygame.init()
        pygame.display.set_caption("AI")
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
                        while(self.MoveCheck(2,1,self.x, self.y, self.next[0])):
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
    neural = Neural_Network()
    neural.run()

if __name__ == "__main__":
    main()