from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

from dachor_internal.models import Profile


class DateInput(TextInput):
    input_type = 'date'


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['email', 'first_name', 'last_name', 'username']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget = DateInput()


class SignupForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': ProfileForm
    }

    def save(self, commit=True):
        objects = super(SignupForm, self).save(commit=False)

        if commit:
            user = objects['user']
            user.is_active = False
            user.save()
            profile = objects['profile']
            profile.user = user
            profile.save()

        return objects
