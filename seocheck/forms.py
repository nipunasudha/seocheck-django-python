from django import forms

class SeocheckForm(forms.Form):
    seoUrl = forms.URLField(label='Quick SEO Checkup - Enter URL ', max_length=500)