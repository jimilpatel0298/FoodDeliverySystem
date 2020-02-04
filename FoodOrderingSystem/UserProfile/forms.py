from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm


class PasswordNew(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordNew, self).__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = '<small id="emailHelp" class="form-text text-muted"><ul><li>Must be of eight characters length.</li><li>Alphanumeric and atleast one uppercase letter and symbol.</li></ul></small>'
        self.fields['new_password2'].help_text = ''

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'


class PasswordReset(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordReset, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email to send instructions'


class PasswordChange(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChange, self).__init__(*args, **kwargs)

        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = '<small id="emailHelp" class="form-text text-muted"><ul><li>Must be of eight characters length.</li><li>Alphanumeric and atleast one uppercase letter and symbol.</li></ul></small>'
        self.fields['new_password2'].help_text = ''

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'

        self.fields['old_password'].label = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password2'].label = ''

        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'password')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = '<small id="emailHelp" class="form-text text-muted">We''ll never share your email with anyone else.</small>'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

        self.fields['username'].label = ''
        self.fields['phone_number'].label = ''
        self.fields['date_of_birth'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Date of Birth'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = '<small id="emailHelp" class="form-text text-muted">We''ll never share your email with anyone else.</small>'
        self.fields['password1'].help_text = '<small id="emailHelp" class="form-text text-muted"><ul><li>Must be of eight characters length.</li><li>Alphanumeric and atleast one uppercase letter and symbol.</li></ul></small>'
        self.fields['password2'].help_text = ''

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['phone_number'].label = ''
        self.fields['date_of_birth'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Date of Birth'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'