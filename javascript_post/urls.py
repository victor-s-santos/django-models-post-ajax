from django.contrib import admin
from django.urls import path, include
from register import views as register_v
from core import views as core_v
from record import views as record_v
from django.conf.urls import url

urlpatterns = [
    #first page
    path('', core_v.index, name='home'),
    #register
    path('register/', register_v.register, name='register'),
    #login
    path('', include('django.contrib.auth.urls')),
    #recording values
    path('record/', record_v.record_value, name='record'),
    #insert record
    url(r'record/insert$', record_v.insert, name='insert'),
    
    #admin
    path('admin/', admin.site.urls),
]
