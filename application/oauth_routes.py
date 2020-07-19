import json

from flask                        import Blueprint, Response, request
from application.config           import Config
from application.logger           import Logger
from application.utils            import Utils

logger =  Logger().get_logger()
oauth  =  Blueprint(
  'oauth',
  __name__,
  url_prefix='/api/oauth',
)

CONFIG          =  Config()
UTILS           =  Utils()


@oauth.route('/lifecheck',  methods=['GET'])
@oauth.route('/lifecheck/', methods=['GET', 'POST'])
def lifecheck():
  app_name     =  CONFIG.app_name
  logging_json =  { 'app_name': app_name }
  logger.info(logging_json)
  return Response(
    headers  =  CONFIG.response_headers,
    response =  json.dumps({
      'appName' :  app_name,
      'stage'   :  CONFIG.stage,
      'path'    :  'api/oauth/lifecheck',
      'status'  :  200
    }))


@oauth.route('/google/redirect',  methods=['GET', 'POST'])
@oauth.route('/google/redirect/', methods=['GET', 'POST'])
def google():
  print(request.__dict__)
  return ''
