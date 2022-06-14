from django import forms

class ex02Form(forms.Form):
    content = forms.CharField(label='Content',required=True, max_length=1000)