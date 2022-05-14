from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.sign_up, name='sign_up'),
    path('signin', views.sign_in, name='sign_in'),
    path('signout', views.sign_out, name='sign_out'),
    path('home', views.home, name='home'),
    path('helping/<slug:issue>/?P<latitude>\d{2}\.\d+?P<longitude>\d{2}\.\d+/', views.helping, name='helping'),
    path('ac_lights/', views.ac_lights, name='ac_lights'),
    path('break_pad_worn/', views.break_pad_worn, name='break_pad_worn'),
    path('dead_battery/', views.dead_battery, name='dead_battery'),
    path('engine_issue/', views.engine_issue, name='engine_issue'),
    path('engine_overheat/', views.engine_overheat, name='engine_overheat'),
    path('flat_tyres/', views.flat_tyres, name='flat_tyres'),
    path('fuel_leak/', views.fuel_leak, name='fuel_leak'),
    path('no_fuel/', views.no_fuel, name='no_fuel'),
    path('others/', views.others, name='others'),
    path('uneven_tyre/', views.uneven_tyre, name='uneven_tyre'),
    path('warning/', views.warning, name='warning'),
]