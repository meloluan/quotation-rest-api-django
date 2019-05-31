from django.contrib import admin

from . import models

# Registrar os modelos aqui
admin.site.register(models.UserProfile)
admin.site.register(models.DroidParts)
