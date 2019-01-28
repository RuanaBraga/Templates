from django.urls import path

from .views import home,cadastros,lista
urlpatterns = [

    path('',home),
    path('/cadastro',cadastros,name='cadastro'),
    path('/lista',lista,name='lista')
]