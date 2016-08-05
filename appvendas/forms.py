from django.forms import ModelForm

from appvendas.models import *
class UnidadeForm(ModelForm):
   class Meta:
       model=Unidade
       fields=('descricao','sigla')
class ProdutoForm(ModelForm):
    class Meta:
        model=Produto
        fields=('descricao','unidade','valorUnitario')

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=('nome','email','telefone','endereco')
