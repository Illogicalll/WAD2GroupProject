from django.urls import path
from resell import views
app_name = 'resell'

urlpatterns = [
path('', views.index, name='index'),
]