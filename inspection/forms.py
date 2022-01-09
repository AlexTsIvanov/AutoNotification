from django.forms import ModelForm,TextInput, Select, DateTimeField
from django.forms.widgets import DateInput
from .models import *

class InspectionForm(ModelForm):

    class Meta:
        model = Inspection
        fields = '__all__'
        widgets = {
            'user' : TextInput(attrs= { 'type': 'hidden'}),
            'vehicle' : TextInput(attrs={ 'type': 'hidden'}),
            'client_telnumber': TextInput(attrs={'class': "form-control", "placeholder" : '0871234567'}),
            'last_check': DateInput(attrs={'class': "form-control", "placeholder" : '2012-12-24'}),
            'next_check': DateInput(attrs={'class': "form-control", "placeholder" : '2012-12-24', 'readonly': 'readonly'}),
            'status' : TextInput(attrs={ 'type': 'hidden', 'value' : 'Inspection Period Not Over'}),
            'email': DateInput(attrs={'class': "form-control", "placeholder" : 'example@abv.bg'})
        }

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'reg_number': TextInput(attrs={'class': "form-control", "placeholder" : 'CA9793PB', }),
            'vehicle_category': Select(attrs={'class': "form-control", "placeholder" : 'Category'}),
            'start_expl': DateInput(attrs={'class': "form-control", "placeholder" : '2012-12-24'}),
        }