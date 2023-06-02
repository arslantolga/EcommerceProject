from django.urls import path
from . import views

app_name = "ecommerce_app"

urlpatterns = [
   
    path('', views.mainpage, name="mainpage" ),
    path('login/', views.login, name="login" ),
    path('signup/', views.signup, name="signup" ),
    path('store/', views.storepage, name="storepage" ),
]