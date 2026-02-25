from django.urls import path
from .views import index, contato, produto, cadastrarProduto, salvarProduto, editarProduto, salvarProduto

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('produto', produto, name='urlproduto'),
    path('cadastrarProduto', cadastrarProduto, name="urlcadastrarProduto"),
    path('salvarProduto', salvarProduto, name="urlsalvarProduto"),
    path('editarProduto/<int:id>', editarProduto, name='urleditarProduto'),
    path('salvarProduto', salvarProduto, name='urlsalvarProduto'),
]