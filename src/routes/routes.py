from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes ={
    "index_route":"/","Indexcontroller":IndexController.as_view("index"),
    "delete_route":"/delete/veiculo/<int:codigo>","delete_controller":DeleteVeiculoController.as_view("delete"),
    "update_route":"/update/veiculo/<int:codigo>","update_controller":UpdateVeiculoController.as_view("update"),    
    "encontro_route":"/encontro","encontro_controller":EncontroController.as_view("encontros"),    
    "delete_encontro_route":"/delete/encontro/<int:codigo>","delete_encontro_controller":DeleteEncontroController.as_view("delete_encontro"),
    "update_route":"/update/veiculo/<int:codigo>","update_controller":UpdateVeiculoController.as_view("update"),    
    "not_found_route":404,"not_found_controller":NotFoundController.as_view("not_found"),
    

}