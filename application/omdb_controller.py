import os
import json
import requests
from datetime   import datetime, timedelta

from application.utils         import Utils
from application.http_requests import Requester
from application.config        import Config
from application.logger        import Logger



class OMDBController:
  def __init__(self):
    self.http_requests =  Requester()
    self.logger        =  Logger().get_logger()
    self.config        =  Config()


  def omdb_request(self, query_string):
    self.logger.debug(f'query_string received: {query_string}')
    res = self.http_requests.get_url(
      url     =  f'{self.config.omdb_base_url}?{query_string}',
      jsonify =  True,
      params  =  {
        'apikey' :  self.config.omdb_api_key,
        'i'      :  self.config.omdb_id,
      },
    )
    return res
