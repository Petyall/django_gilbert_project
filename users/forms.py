from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User, UsersReceipts


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш никнейм'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

    
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Придумайте себе никнейм'
    }))    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите вашу почту'
    }))    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите ваш пароль'
    }))    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите ваш пароль'
    }))    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'
    }), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True
    }))


    class Meta:
        model = User
        fields = ('image', 'username', 'email')


class UserReceiptForm(forms.ModelForm):
    receipt_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Название блюда',
    }))
    cooking_time = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Примерное время приготовления',
    }))
    link = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ссылка на источник (при наличии)',
    }), required=False)
    steps = forms.Textarea()
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'Фотография готового блюда'
    }))


    class Meta:
        model = UsersReceipts
        fields = ('receipt_name', 'cooking_time', 'steps', 'image', 'link')