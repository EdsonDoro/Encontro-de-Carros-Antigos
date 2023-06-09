from flask import Flask
from src.routes.routes import *


app = Flask(__name__)

app.add_url_rule(routes["index_route"],view_func=routes["Indexcontroller"])

app.add_url_rule(routes["delete_route"],view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"],view_func=routes["update_controller"])

app.add_url_rule(routes["encontro_route"],view_func=routes["encontro_controller"])

app.add_url_rule(routes["delete_encontro_route"],view_func=routes["delete_encontro_controller"])

app.add_url_rule(routes["update_encontro_route"],view_func=routes["update_encontro_controller"])

app.register_error_handler(routes["not_found_route"],routes["not_found_controller"])