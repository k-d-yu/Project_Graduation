from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from main.models import Feedback


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': "Email"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'login_input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['surname', 'name', 'patronymic', 'email', 'phoneNumber', 'secondPhoneNumber', 'bio',
                  'date_of_birth', 'profile_image']
        labels = {'surname': 'Фамилия', 'name': 'Имя', 'patronymic': 'Отчество', 'phoneNumber': 'Номер телефона',
                  'secondPhoneNumber': 'Доп. номер телефона', 'bio': 'О себе', 'date_of_birth': 'Дата рождения',
                  'profile_image': 'Фотография'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'login_input'})


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'reviews_text_input'})