from app import init_app
from app.c2b import c2b

config_name = 'default'
application = init_app(config_name)

application.register_blueprint(c2b)


if __name__ == "__main__":
    application.run(debug=True)