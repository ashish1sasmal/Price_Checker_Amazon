from django.urls import path
from . import views

# app_name="price"

urlpatterns = [
    path('price/',views.price,name='price'),
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.register,name='signup'),
]
