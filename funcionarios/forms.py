from django import forms
from funcionarios.models import Funcionario

class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"
