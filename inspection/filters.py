import django_filters
from django_filters import DateFilter, CharFilter
from .models import *
from django.forms import ModelForm,TextInput, Select


class InspectionFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="last_check", lookup_expr= "gte" )
    end_date = DateFilter(field_name="last_check", lookup_expr= "lte" )
    vehicle_num = CharFilter(field_name="vehicle__reg_number", lookup_expr='istartswith')
    class Meta:
        model = Inspection
        fields = {"client_telnumber", "next_check", 'status'}

