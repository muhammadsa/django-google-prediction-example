from django import forms

class CollegeForm(forms.Form):
    SAT = forms.IntegerField(required=True, min_value=600, max_value=2400)
    GPA = forms.DecimalField(required=True, min_value=0.0, max_value=4.0)
    others = forms.IntegerField(required=True, min_value=1, max_value=5)