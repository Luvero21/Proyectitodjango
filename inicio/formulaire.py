from django import forms

class formulaireProducto(forms.Form):
    nombre= forms.CharField(max_length=100)
    descripcion= forms.CharField(widget=forms.Textarea())
    precio=forms.DecimalField(max_digits=6,decimal_places=2)
    imagen=forms.ImageField(required=False)
    stock=forms.IntegerField()
    
    
    
    