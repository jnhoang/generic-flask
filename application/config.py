import os
import json
from application.singleton import Singleton
from dotenv import load_dotenv
load_dotenv('.env.local')

@Singleton
class Config:
  app_name =  'application'
  stage    =  os.getenv('STAGE')
  app_key  =  os.getenv('APP_KEY')

  # omdb values
  omdb_base_url =  'http://www.omdbapi.com'
  omdb_api_key  =  os.getenv('OMDB_API_KEY')
  omdb_id       =  os.getenv('OMDB_ID')

  # marvel values
  marvel_base_url    =  'https://gateway.marvel.com:443'
  marvel_public_key  =  os.getenv('MARVEL_PUBLIC_KEY')
  marvel_private_key =  os.getenv('MARVEL_PRIVATE_KEY')

  # env_vars
  def __init__(self):
    print('config class loaded')


  def something(self):
    pass
