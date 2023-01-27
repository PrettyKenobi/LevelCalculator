import logging

LOGGER = logging.getLogger(__name__)

class LevelCalculator:

  def __init__(self, level=1, experience=0):
    self.previous_level = level
    self.overall_experience = experience
    self.current_level = 0

  def calculate_new_level(self):
    level_progression = [10]
    experience = int(self.overall_experience)
    if experience <= level_progression[0]:
      self.current_level = 1
      return self.current_level
    else:
      while experience > 0:
        level_experience = level_progression[-1]
        next_level_experience = level_experience * 2
        self.current_level += 1
        level_progression.append(next_level_experience)
        experience -= level_experience
    return self.current_level

  def run(self):
    self.calculate_new_level()
        