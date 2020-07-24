from django import forms
from .models import Posts


class CategoryForm(forms.Form):
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class AuthorForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile_No = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'description', 'category', 'author', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput()
        }


class BlogSearch(forms.Form):
    Search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))