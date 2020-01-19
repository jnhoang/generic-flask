import os
import json


class Config:
  # flask settings - declare as class attributes


  # env_vars
  def __init__(self):
    self.response_headers =  {
      'Content-Type'                 : 'application/json',
      'Access-Control-Allow-Origin'  : '*',
    }
    self.app_name = 'application'
    self.stage = 'local'


  def something(self):
    pass
