from django import forms
from django.forms import ModelForm
from .models import House, Section, Floor

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['name_section']
        widgets = {
            'name_section': forms.TextInput(attrs={'class': 'form-control', 'value': 'Section __prefix__'})
        }

class FloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = ['name_floor']
        widgets = {
            'name_floor': forms.TextInput(attrs={'class': 'form-control', 'value': 'Floor __prefix__'})
        }

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['name_home', 'address', 'image1', 'image2', 'image3',  'image4', 'image5', 'staff']
        widgets = {
            'name_home': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text(this)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text(this)'}),
            'image1': forms.FileInput(attrs={'id': 'image1-House', 'onchange': 'add_image(this, "block_for_image1")'}),
            'image2': forms.FileInput(attrs={'id': 'image2-House', 'onchange': 'add_image(this, "block_for_image2")'}),
            'image3': forms.FileInput(attrs={'id': 'image3-House', 'onchange': 'add_image(this, "block_for_image3")'}),
            'image4': forms.FileInput(attrs={'id': 'image4-House', 'onchange': 'add_image(this, "block_for_image4")'}),
            'image5': forms.FileInput(attrs={'id': 'image5-House', 'onchange': 'add_image(this, "block_for_image5")'}),
        }

