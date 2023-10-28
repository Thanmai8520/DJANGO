from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('', views.home_page, name="home1"),
    # path('login/home1/', views.home1, name="login_home1"),

    path('login/', views.login),
    # path('login/logincheck/login/',views.login),
    path('newuser/', views.newuser),

    path('aboutus/', views.aboutus),
    path('aboutagri/', views.aboutagri),
    path('aboutaqua/', views.aboutaqua),


    path('contactus/', views.contactus),
    path('contactus/contactdetails/', views.contactdetails),
    path('contactus/contactdetails/', views.rate),

    path('login/module1/',views.module1),
    path('module1/', views.module1),
    path('module2/', views.module2),
    path('module1/module3/', views.module3),
    path('module1/module3/products/', views.shop),

    path('newuser/regdetails/', views.regdetails),

    path('login/module1/aboutus/', views.aboutus),
    path('module1/aboutus/', views.aboutus),

]
