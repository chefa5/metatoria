from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from users.models import User

class  UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      "placeholder": "Логин"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "placeholder" : "Пароль"}),
    )
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "autofocus": True,
                "placeholder" : "E-mail",
                "value": '',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Имя"
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Логин"
            }
        )
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder" : "Пароль"
            }
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder" : "Повтор пароля"
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "username",
            "password1",
            "password2",
        )

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "about_me",
            "tg_contact",
            "vk_contact",
            "phone_number",
        )
    
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-input",
                

            }
        ), required=False
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Имя",
                "class": "form-input",
            }
        ), required=False
    )
    about_me = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "О себе"
            }
        ), required=False
    )
    tg_contact = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "form-input",
                "placeholder": "Telegram"
            }
        ), required=False
    )
    vk_contact = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "form-input",
                "placeholder": "Вконтакте"
            }
        ), required=False
    )
    phone_number = PhoneNumberField(
        region="RU",
        widget=RegionalPhoneNumberWidget(
            attrs={
                "class": "form-input",
                "placeholder": "Телефон",
                "id": "id_phone_number",
                "default" : "",
            }
        ), required=False
    )