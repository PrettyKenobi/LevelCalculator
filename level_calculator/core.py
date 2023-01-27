from . import helpers

#TODO: add variable typing
def main():
  """
  The module's entry point.

  Return exit status code.
  """
  #TODO: Check for input
  #TODO: Prompt if no input
  experience = input("How much experience do you have overall? ")
  calculator = helpers.LevelCalculator(1,experience)
  print(calculator.calculate_new_level())
  return 0