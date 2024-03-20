from django.urls import path
from .import views
urlpatterns=[
    path('admin/ ',views.adminLogin),
    path('login/ ',views.userLogin,name='login'),
    path('dash/',views.dashboard),
    path('userLogout/', views.userLogout, name='logout'),

]