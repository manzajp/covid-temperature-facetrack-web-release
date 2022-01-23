from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/success/', views.register, name='register_success'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('auth/', views.auth, name='auth'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('account/acc_change', views.acc_change, name='acc_change'),
    path('logout/success/', views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_control, name='logout_control'),
]