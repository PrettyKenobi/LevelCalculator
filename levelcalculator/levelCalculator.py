class LevelCalculator:

  def __init__(self, level=1, experience=0):
    self.previous_level = level - 1
    self.overall_experience = experience
    self.current_level = level

  def calculate_new_level(self):
    level = 1
    experience_required = 10
    experience = self.overall_experience

    while experience >= experience_required:
      experience -= experience_required
      level += 1
      experience_required *= 2

    self.previous_level = self.current_level
    self.current_level = level

  def run(self):
    self.calculate_new_level()