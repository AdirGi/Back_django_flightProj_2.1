from cgitb import html
from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenRefreshView)

 
 
urlpatterns = [
     path('', views.index),
     # products- not connect
     path('products/', views.products),
     path('products/<id>', views.products),

     # customers  
     path('customers/', views.customers),
     path('customers/<id>', views.customers),
     path('get_customers_by_username/', views.get_customers_by_username),

     # countries
     path('countries/', views.countries),
     path('countries/<id>', views.countries),

     # administrators
     path('administrators/', views.administrators),
     path('administrators/<id>', views.administrators),

     # Airline_Companies
     path('airline_companies/', views.Airline_Companies),
     path('airline_companies/<id>', views.Airline_Companies),
     path('get_airline_by_user_id/<id>', views.get_airline_by_user_id),

     # flights
     path('flights/', views.flights),
     path('flights/<id>', views.flights),
     path('get_flights_by_airline_id/', views.get_flights_by_airline_id),

     path('get_flights_by_parameters/', views.get_flights_by_parameters),

     # User_Roles
     path('user_roles/', views.User_Roles),
     path('user_roles/<id>', views.User_Roles),
 
     # Tickets
     path('tickets/', views.Tickets),
     path('tickets/<id>', views.Tickets),

     

    #
    path('getroutes/', views.getRoutes),

    path('addnote/', views.addNote),
    # register/singup
    path('adduser/', views.addUser),

    path('notes/', views.getNotes),
 
    # token login
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

# test1.html
    # login and logout use token
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('logout/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), 

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)