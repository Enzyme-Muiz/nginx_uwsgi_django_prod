from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


appname= "html_only"
urlpatterns = [
    path('', views.homepage, name= "homepage"),
    #path('admin/', admin.site.urls),
    
]