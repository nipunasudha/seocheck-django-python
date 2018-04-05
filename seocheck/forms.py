from django import forms

class SeocheckForm(forms.Form):
    seoUrl = forms.CharField(label='Quick SEO Checkup - Enter URL ', max_length=500)