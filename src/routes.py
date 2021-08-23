"""
API routing
"""
# ==============================================================================


def build_blueprints(api):

    # General Endpoints
    from src.endpoints.general import general  # noqa: E402
    api.blueprint(general, url_prefix='/api/')

    # Bowl Endpoints
    from src.endpoints.bowl import bowl  # noqa: E402
    api.blueprint(bowl, url_prefix='/api/bowl')
