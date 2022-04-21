from django import forms

class articleEdit(forms.Form):
    head = forms.CharField(label="Заголовок")
    body = forms.CharField(label="Статья", widget=forms.Textarea)
