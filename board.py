import pygame
import tiles from tile

class board:
  def drawBoard(self):
    self.window.fill(self.windowBgColor)

    for i in range(self.N):
      rectY = self.blockSize * i + self.gap
      for j in range(self.N):
        rectX = self.blockSize * j + self.gap
        cellValue = int(self.boardStatus[i][j])

        pygame.draw.rect(
          self.window,
          BG_COLORS[cellValue],
          pygame.Rect(rectX, rectY, self.cellSize, self.cellSize)
        )

        if cellValue != 0:
          textSurface = self.myFont.render(f"{cellValue}", True, (0, 0, 0))
          textRect = textSurface.get_rect(center = (rectX + self.blockSize / 2, rectY + self.blockSize / 2))
          self.window.blit(textSurface, textRect)