from django.urls import path
from . import views

urlpatterns=[
    path('bmsapp/',views.bmsapp,name='bmsapp'),
    path('bmsapp/myTicket',views.myTicket,name='myTicket'),
    path('bmsapp/About',views.About,name='About'),
    path('bmsapp/Funalot',views.Funalot,name='Funalot'),
    path('bmsapp/Costsavings', views.Costsavings, name='Costsavings'),
    path('bmsapp/contactUs',views.contactUs,name='contactUs'),
    path('bmsapp/saveMovieData',views.saveMovieData,name='saveMovieData'),
    path('bmsapp/updateBooking/<int:id>',views.updateBooking,name='updateBooking'),
    path('bmsapp/updateBooking/updateBookingData/<int:id>', views.updateBookingData, name='updateBookingData'),
    path('bmsapp/deleteBooking/<int:id>',views.deleteBooking,name='deleteBooking')]