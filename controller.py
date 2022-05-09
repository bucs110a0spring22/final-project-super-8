import pygame
import random
import numpy as np
import tiles from tile

class Controller:
  def __init__(self):
    self.N = 4
    self.cellSize = 80
    self.gap = 4
    self.windowBgColor = (184, 158, 190)
    self.blockSize = self.cellSize + self.gap * 2

  def respawn(self):
    freePos = zip(*np.where(self.boardStatus == 0))
    freePos = list(freePos)

    for pos in random.sample(freePos, k=1):
      self.boardStatus[pos] = 2    

  def Merge(self, numbers):
    result = [0]
    numbers = [x for x in numbers if x != 0]
    for element in numbers:
      if element == result[len(result) - 1]:
        result[len(result) - 1] *= 2
        result.append(0)
      else:
        result.append(element)

    result = [x for x in result if x != 0]
    return result
  
  def move(self, dir):
    for idx in range(self.N):

      if dir in "UD":
        numbers = self.boardStatus[:, idx]
      else:
        numbers = self.boardStatus[idx, :]

      flip = False
      if dir in "RD":
        flip = True
        numbers = numbers[::-1]

      numbers = self.compressNumber(numbers)
      numbers = numbers + (self.N - len(numbers)) * [0]

      if flip:
        numbers = numbers[::-1]

      if dir in "UD":
        self.boardStatus[:, idx] = numbers
      else:
        self.boardStatus[idx, :] = numbers
  
  def isGameOver(self):
    boardStatusBackup = self.boardStatus.copy()
    for dir in "UDLR":
      self.move(dir)

      if (self.boardStatus == boardStatusBackup).all() == False:
        self.boardStatus = boardStatusBackup
        return False
    return True
  
  def play(self):
    running = True
    while running:
      self.drawBoard()
      pygame.display.update()

      for event in pygame.event.get():
        oldBoardStatus = self.boardStatus.copy()
        
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            self.move("U")
          elif event.key == pygame.K_DOWN:
            self.move("D")
          elif event.key == pygame.K_LEFT:
            self.move("L")
          elif event.key == pygame.K_RIGHT:
            self.move("R")
          elif event.key == pygame.K_ESCAPE:
            running = False

          if self.isGameOver():
            print("GAME OVER")
            return
  
          if (self.boardStatus == oldBoardStatus).all() == False:
            self.respawn()
