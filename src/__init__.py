"""
Main API Server
"""
import os
from sanic import Sanic
from sanic_cors import CORS
from sanic.log import logger
from src.config import DevConfig, QAConfig, ProdConfig
from src.errors import apply_error_handler
# from src.models import db
from src.routes import build_blueprints
from src.util import bcolours
# ==============================================================================


def build_api():
    """API Creation & Configuration
    """
    api_build = Sanic(__name__, strict_slashes=False)
    CORS(api_build)

    if 'ENV' not in os.environ:
        raise RuntimeError('Specify ENV for application: "dev" , "qa", or "prod"')
    api_build.config['ENV'] = os.environ['ENV']
    if api_build.config['ENV'] == 'dev':
        print(bcolours.OKGREEN + "\n %% DEV %% \n" + bcolours.ENDC)
        logger.info(" %% DEV %% ")
        api_build.update_config(DevConfig())
    elif api_build.config['ENV'] == 'qa':
        print(bcolours.HEADER + "\n %% QA %% \n" + bcolours.ENDC)
        logger.info(" %% QA %% ")
        api_build.update_config(QAConfig)
    elif api_build.config['ENV'] == 'prod':
        print(bcolours.OKBLUE + "\n %% PROD %% \n" + bcolours.ENDC)
        logger.info(" %% PROD %% ")
        api_build.update_config(ProdConfig)
    else:
        raise RuntimeError('CONFIGURATION STARTUP ERROR\nENV was not properly specified as one of "dev", "qa" or "prod".')

    logger.info("Started up")
    # db.init_app(api_build)
    build_blueprints(api_build)
    apply_error_handler(api_build)
    return api_build


api = build_api()
