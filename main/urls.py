
from django.contrib import admin
from django.urls import path, include
from courier_mgt.views import register, profile

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courier_mgt.urls')),
    path('login/', auth_views.LoginView.as_view(template_name= 'registration/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'registration/logout.html'), name= 'logout'),
    path('profile/', profile, name='site-profile'),
    path('register/', register, name='site-register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)