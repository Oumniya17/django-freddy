# Registro de modelos en el panel de administración
from django.contrib import admin
from .models import Animatronic, Party

# Permite gestionar animatrónicos desde /admin
admin.site.register(Animatronic)

# Permite gestionar fiestas desde /admin
admin.site.register(Party)
