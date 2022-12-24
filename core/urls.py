from django.urls import path
from .views import index,preenchimento,dados_pessoais,add_modal


urlpatterns = [
    path('', index, name='index'),
    path('preenchimento', preenchimento, name='preenchimento'),
    path('dados_pessoais',dados_pessoais,name='dados_pessoais'),
    path('add_modal',add_modal, name='add_modal'),
  
]