from django.contrib import admin
from django.urls import path

import usuarios.views
from usuarios.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

]
