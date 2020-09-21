#from django.contrib import admin
from django.urls import path
#from django.contrib import admin
from . import views

from .views import PageView


urlpatterns = [
    #path(r'admin/', admin.site.urls),
    path('', PageView.as_view()),
    path('<str:template>', PageView.as_view()),
]