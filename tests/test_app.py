from .context import level_calculator
  
def test_low_experience_current_level(at_level_one):
  calculator = level_calculator.helpers.LevelCalculator(1,at_level_one)
  calculator.calculate_new_level()
  assert calculator.current_level == 1

def test_high_experience_current_level( above_level_one):
  calculator = level_calculator.helpers.LevelCalculator(1, above_level_one)
  calculator.calculate_new_level()
  assert calculator.current_level == 3