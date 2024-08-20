from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Cliente
    # nome
    # email
    # telefone
    # usuario

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

# Produto
    # imagem
    # nome
    # preco
    # ativo
    # categoria
    # tipo

# Categorias (Masculino, Feminino, Infantil)
    # nome

# Tipos (Camisa, Camiseta, Bermuda, Calça)
    # nome

# itemestoque
    # produto (ex: camisa)
    # cor (ex: azul, laranja, verde)
    # tamanho (ex: P, M, G)
    # quantidade

# ItensPedido
    # itemestoque (camisa, laranja, M)
    # quantidade (10 itens)

# Pedido
    # cliente
    # data_finalizacao
    # finalizado
    # id_transacao
    # endereco
    # itenspedido

# Endereco
    # rua
    # numero
    # complemento
    # cep
    # cidade
    # estado
    # cliente