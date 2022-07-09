from . import views
from django.urls import path


app_name = "portafolioVirtual"
urlpatterns = [
    path('', views.HomeView.as_view(), name = "home")]