import os
import json
from application.singleton import Singleton
from dotenv import load_dotenv
load_dotenv('.env.local')

@Singleton
class Config:
  app_name      =  'application'
  stage         =  os.getenv('STAGE')

  # omdb values
  omdb_base_url =  'http://www.omdbapi.com'
  omdb_api_key  =  os.getenv('OMDB_API_KEY')
  omdb_id       =  os.getenv('OMDB_ID')


  # env_vars
  def __init__(self):
    print('config class loaded')


  def something(self):
    pass
