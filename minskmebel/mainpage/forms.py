from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'inputbox', 'placeholder' : 'Ваше имя'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'inputbox', 'placeholder' : 'Ваш E-mail'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputbox phone-box', 'placeholder' : 'Ваш телефон'}))
    time = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputbox', 'placeholder' : 'Удобное время для звонка'}))


class SendMessage(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'inputdata'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'inputdata'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'inputdata', 'rows' : '10', 'wrap' : 'hard', 'cols' : '20', 'style': 'height: 25%;'}))
