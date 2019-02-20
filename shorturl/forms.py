from django import forms

class submiturlform(forms.Form):
    url= forms.CharField(label='submit urls' )
