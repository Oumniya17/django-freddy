# Formulario basado en Animatronic
from django import forms
from .models import Animatronic

class AnimatronicForm(forms.ModelForm):
    class Meta:
        model = Animatronic
        fields = ['name', 'animal', 'build_date', 'decommissioned', 'parties']
       # Widgets personalizados
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Animatronic name'}),
            'animal': forms.Select(),
            'build_date': forms.DateInput(attrs={'type': 'date'}),
            'decommissioned': forms.CheckboxInput(),
            'parties': forms.CheckboxSelectMultiple(),
        }

        labels = {
            'name': 'Name',
            'animal': 'Animal type',
            'build_date': 'Build date',
            'decommissioned': 'Decommissioned',
            'parties': 'Parties',
        }

        error_messages = {
            'name': {
                'max_length': 'The name of the animatronic must not be more than 50 characters long',
                'required': 'The name of the animatronic is required',
            },
            'build_date': {
                'required': 'The build date is required',
            },
        }
    # Validación básica del nombre y la fecha de construcción
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if not name:
            raise forms.ValidationError("The name of the animatronic is required")
        if len(name) > 50:
            raise forms.ValidationError("The name of the animatronic must not be more than 50 characters long")
        return name

    def clean_build_date(self):
        build_date = self.cleaned_data.get('build_date', '')
        if not build_date:
            raise forms.ValidationError("The build date is required")
        if len(build_date) > 20:
            raise forms.ValidationError("Build date must be at most 20 characters long")
        return build_date
