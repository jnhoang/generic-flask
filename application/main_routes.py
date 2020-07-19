import json
import pprint
from flask                        import Blueprint, Response, request
from application.config           import Config
from application.logger           import Logger
from application.utils            import Utils
from application.main_controller  import MainController
from application.omdb_controller  import OMDBController

logger         =  Logger().get_logger()
main           =  Blueprint(
  'main',
  __name__,
  url_prefix='/api',
)

CONFIG          =  Config()
UTILS           =  Utils()
MAIN_CONTROLLER =  MainController()
OMDB_CONTROLLER =  OMDBController()


@main.route('/lifecheck',  methods=['GET'])
@main.route('/lifecheck/', methods=['GET', 'POST'])
def lifecheck():
  # MAIN_CONTROLLER.handle_auth(app.current_request)
  # print('request json: ', request.json)
  app_name     =  CONFIG.app_name
  logging_json =  { 'app_name': app_name }
  logger.info(logging_json)
  # if multiple qs for 'search'- params = request.args.getlist('search')
  # have request as dict = request.args.to_dict()

  return Response(
    response =  json.dumps({
      'appName' :  app_name,
      'stage'   :  CONFIG.stage,
      'path'    :  '/main/lifecheck',
      'status'  :  200,
    })
  )


@main.route('/omdb',  methods=['GET'])
@main.route('/omdb/', methods=['GET'])
def test():
  try:
    # convert this to a decorator
    api_key = request.headers.get('x-api-key')
    if api_key != CONFIG.app_key:
      return Response(response='sorry', status=401)

    accepted_params =  ['search_term']
    params          =  request.args
    search_term     =  request.args.get('search_term')
    result          =  OMDB_CONTROLLER.omdb_request(search_term)
    return Response( response=json.dumps(result) )
  except Exception as e:
    print(e)
    return 'boo'

