import os
import json
import requests
from datetime   import datetime, timedelta

from application.http_requests import Requester
from application.config        import Config
from application.logger        import Logger


class MarvelController:
  def __init__(self):
    self.http_requests =  Requester()
    self.logger        =  Logger().get_logger()
    self.config        =  Config()


  def marvel_request(self, query_string):
    self.logger.debug(f'\n\nquery_string received: {query_string}')
    print(f'{self.config.marvel_base_url}/v1/public/characters?{query_string}')
    res = self.http_requests.get_url(
      url     =  f'{self.config.marvel_base_url}/v1/public/characters?{query_string}',
      jsonify =  True,
      params  =  {
        'apikey' :  self.config.marvel_public_key,
      },
    )
    return res
