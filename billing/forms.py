from django import forms

class BillForm(forms.Form):
    reading = forms.FloatField(label="Monthly Water Reading", min_value=0)
    has_sewer = forms.ChoiceField(label="Sewer Connection", choices=[('yes', 'Yes'), ('no', 'No')])
    months = forms.IntegerField(label="Number of Months", min_value=1)