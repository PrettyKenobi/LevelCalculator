import typing

class LevelCalculator:
  """This class does the actual calculations.

  :param level: The character's current level, defaults to 1.
  :type level: int

  :param experience: The character's total amount of experience, defaults to 0.
  :type experience: int
  """

  def __init__(self, level: int=1, experience: int=0):
    """Constructor method
    """
    self.previous_level = level - 1
    self.overall_experience = experience
    self.current_level = level

  def calculate_new_level(self):
    """Calculates the character's new level based on total experience. Currently
    it starts with requireing 10 experience to reace level 2, then doubles the
    amount of expereince for each level after that.
    """
    level = 1
    experience_required = 10
    experience = self.overall_experience

    while experience >= experience_required:
      experience -= experience_required
      level += 1
      experience_required *= 2

    self.previous_level = self.current_level
    self.current_level = level
