from django.urls import path
from textiles import views
app_name = 'textiles'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    # path('', views.home, name='home-paytm'),
    # path('payment/', views.payment, name='payment'),
    # path('response/', views.response, name='response'),
]