from django.urls import path
from catproduto import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('categorias/', views.CategoriaListView.as_view(), name='listallprod'),
    path('categorias/<slug:slugcat>', views.ProdutosListView.as_view(), name='listcategorias'),
    path('categorias/', views.MostraProdutoListView.as_view(), name='proddetalhes'),
]