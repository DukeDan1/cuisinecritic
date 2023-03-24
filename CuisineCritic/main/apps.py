from django.apps import AppConfig
import os
from django.conf import settings

class CuisineCriticConfig(AppConfig):
    name = 'CuisineCritic'
    verbose_name = 'Cuisine Critic'
    label = "Cuisine Critic"
    #path = os.path.join(settings.BASE_DIR, 'main')