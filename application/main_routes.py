import json

from flask                        import Blueprint, Response, request
from application.config           import Config
from application.logger           import Logger
from application.utils            import Utils
from application.main_controller  import MainController

logger         =  Logger().get_logger()
main           =  Blueprint('main', __name__)

CONFIG          =  Config()
UTILS           =  Utils()
MAIN_CONTROLLER =  MainController()


@main.route('/',  methods=['GET'])
def main():
  return (<h1>wow, hello</h1>)

@main.route('/api/lifecheck',  methods=['GET'])
@main.route('/api/lifecheck/', methods=['GET', 'POST'])
def lifecheck():
  # MAIN_CONTROLLER.handle_auth(app.current_request)
  # print('request json: ', request.json)
  app_name     =  CONFIG.app_name
  logging_json =  { 'app_name': app_name }
  logger.info(logging_json)
  return Response(
    headers  =  CONFIG.response_headers,
    response =  json.dumps({'appName': app_name, 'stage': CONFIG.stage, 'path': '/main/lifecheck', 'status': 200}))

