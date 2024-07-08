from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/details/update/<int:id>', views.updaterecord, name='updaterecord'),
    path('members/details/member_change_active/<int:id>', views.member_change_active, name='member_change_active'),
]