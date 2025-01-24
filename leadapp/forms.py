from leadapp.models import LEAD
from django import forms

class LeadForm(forms.Modelform):

    class Meta:

        model=LEAD
        fields="__all__"

