import pygame
import random

# テトリスのゲームクラス
class Tetris:
    next_count = -1
    val = [0,1,2,3,4,5,6]
    dir = 0

    def __init__(self):
        pygame.init()
        self.score = 0
        self.line = 0
        self.block = [
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
            [0,7,0,0]]],
        ]
        self.screen_width, self.screen_height = 300, 600
        self.screen = pygame.display.set_mode((self.screen_width*2, self.screen_height))
        self.clock = pygame.time.Clock()
        self.block_size = self.screen_width // 10
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.current_block = self.block[self.nextDecide()]
        self.current_block_x = 3
        self.current_block_y = 0
        self.game_over = False
        self.block_colors = {
            1: (0, 255, 255),
            2: (255, 255, 0),
            3: (0, 255, 0),
            4: (255, 0, 0),
            5: (0, 0, 255),
            6: (255, 128, 0),
            7: (127, 0, 255),
        }
        

    # ランダムなブロックを取得する関数
    def nextDecide(self):
        if(self.next_count == -1):
            random.shuffle(self.val)
        self.next_count += 1
        if self.next_count == 7:
            random.shuffle(self.val)
            self.next_count = 0
        return int(self.val[self.next_count])

    
    # ブロックを描画する関数
    def draw_block(self):
        for y in range(4):
            for x in range(4):
                if self.current_block[self.dir][y][x] != 0:
                    block_type = self.current_block[self.dir][y][x] 
                    block_color = self.block_colors[block_type]  # ブロックの色を取得

                    pygame.draw.rect(self.screen, block_color, ((self.current_block_x + x) * self.block_size, (self.current_block_y + y) * self.block_size, self.block_size, self.block_size))

    # ブロックを移動する関数
    def move_block(self, x, y):
        if not self.check_collision(self.current_block, self.current_block_x + x, self.current_block_y + y):
            self.current_block_x += x
            self.current_block_y += y

    # ブロックの衝突判定を行う関数
    def check_collision(self, direction, ):
        dirx = 0
        diry = 0
        checked = { false, false, false, false}
        for i in range(4):
            for j in range(4):
                if direction == 0:
                    diry = i
                    dirx = j
                    break
                elif direction == 1:
                    diry = j
                    dirx = 3-i
                    break
                elif direction == 2:
                    diry = 3-i
                    dirx = j
                    break
                elif direction == 3:
                    diry = j
                    dirx = i
                    break
            
                if direction == 0:
                    if (field[diry + y - power + FIELD_SPACE - 1 + srsy, dirx + x + FIELD_WALL + srsx] != 0 and !chked[j]:
                            return false;



    # 一列揃ったら消す関数
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if 0 not in row]
        for line in lines_to_clear:
            del self.board[line]
            self.board.insert(0, [0 for _ in range(10)])
            self.score += 100

    # ブロックを時計回りに90度回転させる関数
    def rotate_block(self):
        if self.dir == 3:
            self.dir = 0
        else:
            self.dir += 1

    # ブロックを反時計回りに90度回転させる関数
    def rotate_block_counter_clockwise(self):
        if self.dir == 0:
            self.dir = 3
        else:
            self.dir -= 1

    # ブロックを固定する関数
    def lock_block(self):
        self.draw_block()
        self.clear_lines()

    # ゲームオーバーかどうかをチェックする関数
    def check_game_over(self):
        return self.check_collision(self.current_block, self.current_block_x, self.current_block_y)

    #ゲームオーバーしたらリセットする関数（学習用）
    def reset(self):
        self.run()

    # ゲームのメインループ（プレイ用）
    def run(self):
        # ゲームのメインループ
        self.score = 0
        self.line = 0
        last_fall_time = 0
        fall_speed = 1000  # ミリ秒単位で1秒ごとにブロックを落とす
        lag_time = 4000  # ラグの時間を設定 (ミリ秒単位)
        lag_end_time = 0  # ラグの終了時間を初期化
        flag_drop_to_bottom = False

        while not self.game_over:
            current_time = pygame.time.get_ticks()
            delta_time = current_time - last_fall_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.move_block(-1, 0)
                    elif event.key == pygame.K_d:
                        self.move_block(1, 0)
                    elif event.key == pygame.K_s:
                        self.move_block(0, 1)
                        self.score += 2
                    elif event.key == pygame.K_w:
                        flag_drop_to_bottom = True
                        while not self.check_collision(self.current_block, self.current_block_x, self.current_block_y + 1):
                            self.current_block_y += 1
                            self.score += 2
                        self.lock_block()
                        self.current_block = self.block[self.nextDecide()]
                        self.current_block_x = 3
                        self.current_block_y = 0
                        if self.check_game_over():
                            self.game_over = True
                        flag_drop_to_bottom = False
                        last_fall_time = current_time
                    elif event.key == pygame.K_RIGHT:  # 「→」ボタンを時計回りの回転操作に割り当てる例
                        self.rotate_block()
                    elif event.key == pygame.K_LEFT:  # 「←」ボタンを反時計回りの回転操作に割り当てる例
                        self.rotate_block_counter_clockwise()

            if delta_time >= fall_speed:
                if flag_drop_to_bottom == False:
                    if not self.check_collision(self.current_block, self.current_block_x, self.current_block_y + 1):
                        self.current_block_y += 1
                        last_fall_time = current_time  # ブロックを移動した時間を更新
                    else:
                        if current_time - lag_end_time >= lag_time:  # ラグ時間を超えたらブロックを固定
                            self.lock_block()
                            self.current_block = self.block[self.nextDecide()]
                            self.current_block_x = 3
                            self.current_block_y = 0
                            if self.check_game_over():
                                self.game_over = True
                            last_fall_time = current_time

            self.screen.fill((0, 0, 0))
            for y in range(len(self.board)):
                for x in range(len(self.board[y])):
                    if self.board[y][x] != 0:
                        pygame.draw.rect(self.screen, (255, 255, 255), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
            self.draw_block()
            pygame.draw.line(self.screen, (255, 255, 255), (300,0), (300,600), 2)
            # フォントの設定
            font = pygame.font.Font(None, 36)  # Noneはデフォルトフォントを使用

            # テキストの内容と色
            text_content1 = "Score : " + str(self.score)
            text_content2 = "Line : " + str(self.line)
            text_color = (255,255,255)

            # テキストを描画
            text_surface1 = font.render(text_content1, True, text_color)
            text_surface2 = font.render(text_content2, True, text_color)
            # テキストの位置
            text_rect1 = text_surface1.get_rect(center=(450, 200))
            text_rect2 = text_surface2.get_rect(center=(450, 400))
            self.screen.blit(text_surface1, text_rect1)
            self.screen.blit(text_surface2, text_rect2)
            pygame.display.flip()
            self.clock.tick(6000)

        if self.game_over:
            print("Score : " + str(self.score))
            print("Line : " + str(self.line))

    ##############################################
    #評価関数
    def evaluate_board(self):
        # 評価基準を組み合わせて総合的な評価を行う
        height_penalty = -0.5 * max_height(state)
        hole_penalty = -0.1 * count_holes(state)
        clear_bonus = 1.0 * lines_cleared(state)

        # 各評価基準に対するペナルティやボーナスを組み合わせて総合的な評価を計算
        evaluation = height_penalty + hole_penalty + clear_bonus

        return evaluation
    


    # ゲームのメインループ（機械学習用）
    def ai_run(self):
        # ゲームのメインループ
        last_fall_time = 0
        fall_speed = 1000  # ミリ秒単位で1秒ごとにブロックを落とす
        lag_time = 4000  # ラグの時間を設定 (ミリ秒単位)
        lag_end_time = 0  # ラグの終了時間を初期化
        flag_drop_to_bottom = False

        while not self.game_over:
            current_time = pygame.time.get_ticks()
            delta_time = current_time - last_fall_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
            
            #AIの行動選択（ランダム）
            ai_action = random.choice([1,2,3,4,5,6])

            # 行動の前に1秒待つ
            pygame.time.delay(50)

            if ai_action == 1:
                self.move_block(-1, 0)
            elif ai_action == 2:
                self.move_block(1, 0)
            elif ai_action == 3:
                self.move_block(0, 1)
                self.score += 2
            elif ai_action == 4:
                flag_drop_to_bottom = True
                while not self.check_collision(self.current_block, self.current_block_x, self.current_block_y + 1):
                    self.current_block_y += 1
                    self.score += 2
                self.lock_block()
                self.current_block = self.block[self.nextDecide()]
                self.current_block_x = 3
                self.current_block_y = 0
                if self.check_game_over():
                    self.game_over = True
                flag_drop_to_bottom = False
                last_fall_time = current_time
            elif ai_action == 5:  # 「→」ボタンを時計回りの回転操作に割り当てる例
                self.rotate_block()
            elif ai_action == 6:  # 「←」ボタンを反時計回りの回転操作に割り当てる例
                self.rotate_block_counter_clockwise()

            if delta_time >= fall_speed:
                if flag_drop_to_bottom == False:
                    if not self.check_collision(self.current_block, self.current_block_x, self.current_block_y + 1):
                        self.current_block_y += 1
                        last_fall_time = current_time  # ブロックを移動した時間を更新
                    else:
                        if current_time - lag_end_time >= lag_time:  # ラグ時間を超えたらブロックを固定
                            self.lock_block()
                            self.current_block = self.block[self.nextDecide()]
                            self.current_block_x = 3
                            self.current_block_y = 0
                            if self.check_game_over():
                                self.game_over = True
                            last_fall_time = current_time

            self.screen.fill((0, 0, 0))
            for y in range(len(self.board)):
                for x in range(len(self.board[y])):
                    if self.board[y][x] != 0:
                        pygame.draw.rect(self.screen, (255, 255, 255), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
            self.draw_block()
            pygame.draw.line(self.screen, (255, 255, 255), (300,0), (300,600), 2)
            # フォントの設定
            font = pygame.font.Font(None, 36)  # Noneはデフォルトフォントを使用

            # テキストの内容と色
            text_content1 = "Score : " + str(self.score)
            text_content2 = "Line : " + str(self.line)
            text_color = (255,255,255)

            # テキストを描画
            text_surface1 = font.render(text_content1, True, text_color)
            text_surface2 = font.render(text_content2, True, text_color)
            # テキストの位置
            text_rect1 = text_surface1.get_rect(center=(450, 200))
            text_rect2 = text_surface2.get_rect(center=(450, 400))
            self.screen.blit(text_surface1, text_rect1)
            self.screen.blit(text_surface2, text_rect2)
            pygame.display.flip()
            self.clock.tick(6000)

        if self.game_over:
            print("Score : " + str(self.score))
            print("Line : " + str(self.line))
            pygame.display.flip()
            self.clock.tick(6000)


# メイン関数
def main():
    tetris_game = Tetris()
    tetris_game.run()

if __name__ == "__main__":
    main()
