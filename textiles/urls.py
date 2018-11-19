from django.urls import path
from textiles import views
app_name = 'textiles'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
]