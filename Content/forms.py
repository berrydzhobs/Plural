from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from Content.models import App
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class CommentBForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-width-1-1    uk-form-small uk-text-meta brt rounded-sm ','placeholder':'Add Comment'}),label=False)

    class Meta:
        model = App
        fields = ['comment']





#Contents Categories
VideoCategory_list = (
  ("Film & Animation", "Film & Animation"),
  ("Autos & Vehicles", "Autos & Vehicles"),
  ("Music", "Music"),
  ("Pets & Animals", "Pets & Animals"),
  ("Sports", "Sports"),
  ("Travel & Events", "Travel & Events"),
  ("Gaming", "Gaming"),
  ("People & Blogs", "People & Blogs"),
  ("Comedy", "Comedy"),
  ("Entertainment", "Entertainment"),
  ("News & Politics", "News & Politics"),
  ("Howto & Style ", "Howto & Style"),
  ("Education", "Education"),
  ("Science & Technology", "Science & Technology"),
  ("Nonprofits & Activism", "Nonprofits & Activism"),
  )


class AppForm(forms.ModelForm):
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
            })
    )

    class Meta:
        model = App
        fields = ['description']


#Getting Username and Password{"C = as Capital letter"}
#======================================================
class CreateAppForm(ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'class':'uk-input bg-pH','placeholder':'Add title'}),label=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'uk-textarea bg-pH','rows':'7','placeholder':'Add description'}),label=False)
    media = forms.ImageField(widget=forms.FileInput(attrs={'accept':'image/*','capture':'user','class':'uk-input bg-secondary','placeholder':'Thumbnail'}),label=False, required=False)
    tags = forms.CharField()

    class Meta:
      model = App
      fields = ['title','description', 'media', 'tags']



