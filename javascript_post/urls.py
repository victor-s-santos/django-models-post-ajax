from django.contrib import admin
from django.urls import path, include
from register import views as register_v
from core import views as core_v

urlpatterns = [
    #first page
    path('', core_v.index, name='home'),
    #register
    path('register/', register_v.register, name='register'),
    #login
    path('', include('django.contrib.auth.urls')),
    #admin
    path('admin/', admin.site.urls),
]
