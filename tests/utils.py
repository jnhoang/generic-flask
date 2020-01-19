from application.config import Config

# this file is used to create mock items for the tests
class Utils:
  def __init__(self):
    self.config = Config()


  def test(self):
    return 'hello'
