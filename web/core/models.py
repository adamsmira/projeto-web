from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    estoque = models.CharField(max_length=100)
    fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class NotaFiscal(models.Model):
    numero = models.CharField(max_length=20)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    produtos = models.ManyToManyField(Produto, through='NotaFiscalProduto')

    def __str__(self):
        return f"Nota {self.numero} - {self.cliente.nome}"

class NotaFiscalProduto(models.Model):
    nota_fiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"