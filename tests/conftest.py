import logging
import pytest

LOGGER = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def example_fixture():
  LOGGER.info("Setting up example fixture")
  yield
  LOGGER.info("Tearing down example fixture")

@pytest.fixture
def at_level_one():
  return 5

@pytest.fixture
def above_level_one():
  return 35