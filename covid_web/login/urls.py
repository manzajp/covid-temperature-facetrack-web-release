from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.LandingView, name='landing'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('auth/', views.auth, name='auth'),

    # path('success/', views.SuccessView.as_view(), name='success'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]