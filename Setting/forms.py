from django import forms
from Profile.models import Profile

class UpdateAccountForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Enter username ','autocomplete':'off'}),)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Enter name ','autocomplete':'off'}),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'uk-input bg-secondary','placeholder':'Enter password ','autocomplete':'off'}),)

class DeleteAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'uk-input bg-secondary','placeholder':'Enter password ','autocomplete':'off'}), label=False)


class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'uk-input bg-secondary','placeholder':'Enter password ','autocomplete':'off'}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'uk-input bg-secondary','placeholder':'Enter password ','autocomplete':'off'}),)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'category', 'biography', 'url']