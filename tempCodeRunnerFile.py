for y in range(len(self.board)):
                for x in range(len(self.board[y])):
                    if self.board[y][x] != 0:
                        pygame.draw.rect(self.screen, (255, 255, 255), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
