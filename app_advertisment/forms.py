from django import forms

class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}))
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control form-control-lg"}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control form-control-lg"}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}))

    def clean_title(self):
        data = self.cleaned_data['title']
        if data.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return data