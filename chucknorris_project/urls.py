from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from jokes import views as jokes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', include('jokes.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', jokes_views.register, name='register'),
]
