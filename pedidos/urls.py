from django.urls import path

from pedidos import views

urlpatterns = [
    path('add/', views.PedidosCreateView.as_view(), name='addpedido'),
    path('resumo/', views.ResumoPedidoTemplateView.as_view(), name='resumopedido'),
    path('resumo/', views.MeuPedidoTemplateView.as_view(), name='meupedido'),

]