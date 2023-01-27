from django.urls import path
from .views import index,preenchimento,dados_pessoais,add_modal,calculo,registro, modalcalc1


urlpatterns = [
    path('', index, name='index'),
    path('preenchimento', preenchimento, name='preenchimento'),
    path('dados_pessoais',dados_pessoais,name='dados_pessoais'),
    path('add_modal',add_modal, name='add_modal'),
    path('modal_calc1/',modalcalc1,name='modal_calc'),
    path('calculo/<int:pk>/',calculo,name='calculo'),
    path('registro/',registro,name='regiustro'),
  
]