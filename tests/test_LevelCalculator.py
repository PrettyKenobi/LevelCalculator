import pytest

from level_calculator import *


class Test_LevelCalculator:
    def test_IncreaseLevelByOne(self):
        newExperience = 20
        calculate = LevelCalculator(1, 0)

        calculate.overall_experience = newExperience
        calculate.calculate_new_level()

        assert calculate.current_level == 2
