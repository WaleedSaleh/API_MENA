from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('get-all/', views.BTCList.as_view(), name="get_all"),
    path('now/', views.ForceExchangeRate.as_view(), name="force_task")
]