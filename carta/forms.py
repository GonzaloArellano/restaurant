from django import forms
from .models import Menu

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }