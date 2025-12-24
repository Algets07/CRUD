from django.contrib import admin
from .models import movie
# Register your models here.

from django.utils.html import format_html

class moviecustomPannel(admin.ModelAdmin):
    list_display = ('name','desc','img','id')

    def img(self,obj):
        return format_html('<img src="{0}" width="200px" height="100px">'.format(obj.img.url))






admin.site.register(movie,moviecustomPannel)