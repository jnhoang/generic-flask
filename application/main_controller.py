import os
import json
import requests
from datetime   import datetime, timedelta

from application.utils         import Utils
from application.http_requests import Requester
from application.config        import Config
from application.logger        import Logger

logger = Logger().get_logger()


class MainController:
  def __init__(self):
    self.http_requests =  Requester()
    self.config        =  Config()

  def test(self):
    pass
