from django.urls import path
from .import views
urlpatterns=[

    path('home/',views.home,name='home'),
    path('registerpage/',views.registerpage,name='register'),
    path('register/',views.register),
    path('',views.loginpage,name='login'),
    path('login/',views.login),
    path('home/fabout/',views.aboutus),
    path('home/rooms/',views.rooms,name='details'),
    path('home/rooms/bookingform/',views.booking),
    path('home/contactus/',views.contactus),
    path('home/testimonials/',views.testimonials)
]