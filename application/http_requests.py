import requests
from requests.auth import HTTPBasicAuth

from application.logger import Logger
from application.config import Config
logger = Logger().get_logger()


class Requester:
  def __init__(self):
    self.config =  Config()

  def get_url(self, url, jsonify, headers={'content': 'application/json'}, verify=True):
    # make GET request
    try:
      response = requests.get(url, headers=headers, verify=verify)
      response.raise_for_status()
    except requests.exceptions.HTTPError as e:
      logger.exception(f'AviaryRequests.get_url Exception: {e}')
      raise e

    # jsonify response
    if jsonify:
      response = self.jsonify_response(response)

    return response


  def jsonify_response(self, response):
    try:
      return response.json()
    except Exception as e:
      logger.exception('Could not jsonify response')
      raise e


  def post_url(self, url, jsonify, payload, auth=None, headers={'content': 'application/json'}, verify=True):
    try:
      response = requests.post(url=url, auth=auth, headers=headers, json=payload, verify=verify)
      response.raise_for_status()
    except requests.exceptions.HTTPError as e:
      logger.exception(f'AviaryRequests.post_url exception: {e}')
      raise e

    if jsonify:
      response = self.jsonify_response(response)

    return response
