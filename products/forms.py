from django import forms

from products.models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments

        fields = ("text", )

        widgets = {
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Escribe tu comentario'
            })
        }