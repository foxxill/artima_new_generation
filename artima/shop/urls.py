from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views



app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    # path('category&<str:category_slug>/', views.category, name = 'category'),
    path('profile/', views.profile, name = 'profile'),
    # path('register/', views.register, name = 'register'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    # path('profile/addproduct/', views.add_product, name='add_product'),
    # path('<str:user>&author', views.profile_pub, name = 'profile_pub'),
    # path('search/', views.search, name = 'search'),
]

