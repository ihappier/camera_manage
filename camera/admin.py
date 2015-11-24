from django.contrib import admin
from .models import *

# Register your models here.


class CameraAdmin(admin.ModelAdmin):
    list_display = ('ip_address_camera',
                    'address_camera',
                    'status_camera',
                    'server_camera',
                    'brand_camera',
                    'date_camera',)
    list_filter = ('status_camera', 'server_camera', 'brand_camera')
    search_fields = ('ip_address_camera', 'address_camera', )


class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address_server', 'status_server', 'comments_server', 'date_server')
admin.site.register(Camera, CameraAdmin)
admin.site.register(Server, ServerAdmin)
