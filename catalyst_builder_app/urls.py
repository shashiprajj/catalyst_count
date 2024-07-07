from django.urls import path, include
from . import views

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('', views.base, name='base'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_data, name='upload_data'),
    path('query/', views.query_builder, name='query_builder'),
    path('api/query-data/', views.query_data, name='query_data'),
    path('users/', views.user_list, name='user_list'),
]

