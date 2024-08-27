from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Sale

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    user_type = forms.ChoiceField(choices=[('', 'Select'), ('Turkish', 'Turkish'), ('Foreign', 'Foreign')])
    tckn = forms.CharField(max_length=11, required=False, label='TC Kimlik Numarası')
    passport_number = forms.CharField(max_length=9, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'user_type', 'tckn', 'passport_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
            Customer.objects.create(user=user, tckn=self.cleaned_data.get('tckn'), passport_number=self.cleaned_data.get('passport_number'))
        return user
    
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = []  # Eğer belirli alanlarınız varsa buraya ekleyebilirsiniz. Şu anda sadece modeli kullanıyoruz.