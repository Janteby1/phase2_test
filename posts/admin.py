from django.contrib import admin
from .models import WCard, BCard

class AuthorAdmin(admin.ModelAdmin):
    pass

# add the models you want in your admin backend
admin.site.register(WCard)
admin.site.register(BCard)
