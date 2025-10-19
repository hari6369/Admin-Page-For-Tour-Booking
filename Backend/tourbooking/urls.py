from django.contrib import admin
from django.urls import path
from mytour import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login, name='login'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('view_booking/', views.View_Booking, name='view_booking'),
    path('view_booking_details/', views.View_Booking_Details, name='view_booking_details'),
    path('user_profile/', views.User_Profile, name='user_profile'),
    path('manage_tour/', views.Manage_Tour, name='manage_tour'),
    path('edit_tour/<int:tour_id>/', views.Add_Edit, name='edit_tour'),
    path('delete_tour/<int:id>/', views.delete_tour, name='delete_tour'),
    path('add_edit/', views.Add_Edit, name='add_edit'),
    path('logout/', views.Logout, name='logout'),
]
