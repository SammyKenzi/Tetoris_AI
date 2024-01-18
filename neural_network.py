import Tetris
import pygame
from pygame.locals import *
import random
import numpy
import sys

class Neural_Network():
    def __init__(self):
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
            neural_sum += x_i * w_i
        neural_sum += bias
        return neural_sum

    # 外部情報を取得する関数
    def get_input(self):
        print(tetris_game.Field)
    
    # 出力層の値を返す関数
    def learn(self):
        # 外部情報のlist x　を取得
        x = self.get_input()
        # 入力層→中間層
        middle_x = []
        for i in range(self.layers[1]):
            middle_x.append(self.summation(x, self.weights[0], self.biases[0]))
        # 中間層→出力層
        return self.summation(middle_x, self.weights[1], self.biases[1])

# メイン関数
def main():
    tetris_game = Tetris.Tetris()
    tetris_game.run()

if __name__ == "__main__":
    main()