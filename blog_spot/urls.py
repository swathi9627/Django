from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('signup/',views.signup, name = 'signup'),
    path('signin/',views.signin, name = 'signin'),
    path('userpg/<str:usr>',views.user_page, name = 'user_pg'),
    path('readerpg/<str:usr>',views.view_page, name = 'reader_pg'),
    path('bloggerpg/<str:usr>',views.blogger_signup, name = 'blogger_pg'),
]