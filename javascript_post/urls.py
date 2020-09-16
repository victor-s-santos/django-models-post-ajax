from django.contrib import admin
from django.urls import path, include
from register import views as register_v
from core import views as core_v
from record import views as record_v

urlpatterns = [
    #first page
    path('', core_v.index, name='home'),
    #register
    path('register/', register_v.register, name='register'),
    #login
    path('', include('django.contrib.auth.urls')),
    #recording values
    path('record/', record_v.record_value, name='record'),
    #admin
    path('admin/', admin.site.urls),
]
