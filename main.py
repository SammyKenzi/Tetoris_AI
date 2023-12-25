import pygame
import random

# テトリスのゲームクラス
class Tetris:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 300, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.block_size = self.screen_width // 10
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.current_block = self.get_random_block()
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
    def get_random_block(self):
        blocks = [
            [[1, 1, 1, 1]],
            [[2, 2], [2, 2]],
            [[0, 3, 3], [3, 3, 0]],
            [[4, 4, 0], [0, 4, 4]],
            [[5, 0, 0], [5, 5, 5]],
            [[0, 0, 6], [6, 6, 6]],
            [[0, 7, 0], [7, 7, 7]],
            
        ]
        return random.choice(blocks)


    
    # ブロックを描画する関数
    def draw_block(self):
        for y in range(len(self.current_block)):
            for x in range(len(self.current_block[y])):
                if self.current_block[y][x] != 0:
                    block_type = self.current_block[y][x]  # ブロックの種類を取得
                    block_color = self.block_colors[block_type]  # ブロックの色を取得

                    pygame.draw.rect(self.screen, block_color, ((self.current_block_x + x) * self.block_size, (self.current_block_y + y) * self.block_size, self.block_size, self.block_size))

    # ブロックを移動する関数
    def move_block(self, x, y):
        if not self.check_collision(self.current_block, self.current_block_x + x, self.current_block_y + y):
            self.current_block_x += x
            self.current_block_y += y

    # ブロックの衝突判定を行う関数
    def check_collision(self, block, x, y):
        for row in range(len(block)):
            for col in range(len(block[row])):
                if block[row][col] != 0:
                    if (
                        y + row >= len(self.board) or
                        x + col < 0 or x + col >= len(self.board[0]) or
                        self.board[y + row][x + col] != 0
                    ):
                        return True
        return False

    # 一列揃ったら消す関数
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if 0 not in row]
        for line in lines_to_clear:
            del self.board[line]
            self.board.insert(0, [0 for _ in range(10)])

    # ブロックを時計回りに90度回転させる関数
    def rotate_block(self):
        rotated_block = [[self.current_block[y][x] for y in range(len(self.current_block))] for x in range(len(self.current_block[0]) - 1, -1, -1)]
        if not self.check_collision(rotated_block, self.current_block_x, self.current_block_y):
            self.current_block = rotated_block

    # ブロックを反時計回りに90度回転させる関数
    def rotate_block_counter_clockwise(self):
        rotated_block = [[self.current_block[x][y] for x in range(len(self.current_block))] for y in range(len(self.current_block[0]) - 1, -1, -1)]
        if not self.check_collision(rotated_block, self.current_block_x, self.current_block_y):
            self.current_block = rotated_block

    # ブロックを固定する関数
    def lock_block(self):
        for y in range(len(self.current_block)):
            for x in range(len(self.current_block[y])):
                if self.current_block[y][x] != 0:
                    # ブロックが固定された後、盤面にブロックの種類情報を保持する
                    self.board[self.current_block_y + y][self.current_block_x + x] = self.current_block[y][x]
        self.clear_lines()

    # ラインを削除する関数
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if 0 not in row]
        for line in lines_to_clear:
            del self.board[line]
            self.board.insert(0, [0 for _ in range(10)])

    # ゲームオーバーかどうかをチェックする関数
    def check_game_over(self):
        return self.check_collision(self.current_block, self.current_block_x, self.current_block_y)

    # ゲームのメインループ
    def run(self):
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.move_block(-1, 0)
                    elif event.key == pygame.K_d:
                        self.move_block(1, 0)
                    elif event.key == pygame.K_s:
                        self.move_block(0, 1)
                    elif event.key == pygame.K_w:
                        flag_drop_to_bottom = True
                        while not self.check_collision(self.current_block, self.current_block_x, self.current_block_y + 1):
                            self.current_block_y += 1
                        self.lock_block()
                        self.current_block = self.get_random_block()
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
                            self.current_block = self.get_random_block()
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
            pygame.display.flip()
            self.clock.tick(6000)

# メイン関数
def main():
    tetris_game = Tetris()
    tetris_game.run()

if __name__ == "__main__":
    main()
