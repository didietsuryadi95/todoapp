from django import forms
from .models import Todo


class TodoForm(forms.Form):
    content = forms.CharField(
        label='Content',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'id':'content'})
    )
    status = forms.ChoiceField(
        label='Status',
        choices=Todo.STATUS_TYPE,
        widget=forms.TextInput(attrs={'class':'form-control', 'id':'content'})
    )