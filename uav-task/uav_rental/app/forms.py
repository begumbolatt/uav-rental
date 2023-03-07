from django import forms
from . import models

class UAVForm(forms.ModelForm):

    class Meta:
        model = models.UAV
        fields = ('brand', 'model', 'weigth', 'category')
        labels = {
            'brand': 'Brand',
            'model': 'Model',
            'weigth': 'Weigth',
            'category': 'Category',
        }
    
    def __init__(self, *args, **kwargs):
        super(UAVForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        