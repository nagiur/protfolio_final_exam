from django import forms
from .models import Category, Projects, cv, SkillModel, Contact, review, blog

class cvform(forms.ModelForm):
    class Meta:
        model = cv
        fields = '__all__'


class catagoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
class projectform(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
class sakillform(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = '__all__'

class contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
class revewfrom(forms.ModelForm):
    class Meta:
        model = review
        fields = ['name', 'rating']
class blogfrom(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'
        