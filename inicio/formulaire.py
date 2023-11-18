from django import forms
from ckeditor.fields import RichTextFormField

class formulaireProducto(forms.Form):
    nombre= forms.CharField(max_length=100)
    descripcion= RichTextFormField()
    precio=forms.DecimalField(max_digits=6,decimal_places=2)
    imagen=forms.ImageField(required=False)
    stock=forms.IntegerField()
    fecha=forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    

    
    
    