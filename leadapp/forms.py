from leadapp.models import LEAD

from django import forms

class LeadForm(forms.ModelForm):

    class Meta:



        model=LEAD

        fields="__all__"

