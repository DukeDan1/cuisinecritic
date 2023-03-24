from django.apps import AppConfig
from CuisineCritic.CuisineCritic.settings import BASE_DIR    

class CuisineCriticConfig(AppConfig):
    name = 'CuisineCritic'
    verbose_name = 'Cuisine Critic'
    label = "Cuisine Critic"
    path = BASE_DIR+"/main"