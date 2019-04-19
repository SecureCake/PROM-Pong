NUMBER_VALUES = [
  [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
  [(0, 0), (0, 1), (0, 1), (1, 1), (2, 1), (3, 1), (4, 0), (4, 1), (4, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 0), (2, 1), (3, 0), (4, 0), (4, 1), (4, 2)],
  [(0, 0), (0, 1), (0, 2), (2, 1), (2, 0), (1, 2), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
  [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 0), (1, 0), (2, 0), (2, 1)],
  [(0, 0), (0, 1), (0, 2), (1, 0), (2, 1), (2, 2), (2, 0), (3, 2), (4, 2), (4, 1), (4, 0)],
  [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 2), (3, 2), (4, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2), (2, 1)],
  [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)]
]

class Number:
  def __init__ (self, value, x, y, colour):
    self.height = 5
    self.width = 3
    self.value = value
    self.x = x
    self.y = y
    self.colour = colour
  
  def setValue (self, value):
    self.value = value
  
 
  def render (self):
    output = {}
    digits = str(self.value)

    for i, digit in enumerate(digits):
      output.update({
        (x + self.x + (self.width + 1) * i, y + self.y): self.colour
        for y, x in NUMBER_VALUES[int(digit)]
      })

    return output

  def getDigit(self, n):
    if  self.value - 10 ** n < 0:
      return False
    
    return self.value // 10 ** n % 10