import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.contents = []  
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
  
  def draw(self, num_balls):
    if num_balls <= len(self.contents):
      draw_list = [self.contents.pop(random.randrange(len(self.contents))) for i in range(num_balls)]
      return draw_list
    else:
      return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls_draw = new_hat.draw(num_balls_drawn)
    count = 0
    for key, value in expected_balls.items():
      if balls_draw.count(key) >= value:
        count += 1
    if count == len(expected_balls):
      M += 1
  probability = M / num_experiments      
  return probability        
