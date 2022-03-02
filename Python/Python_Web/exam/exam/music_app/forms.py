from django import forms

from exam.music_app.models import Profile, Album


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.NumberInput(

                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class DeleteProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance


class AddAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'description': forms.Textarea(

                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(

                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(

                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class EditAlbum(AddAlbum):
    pass


class DeleteAlbum(AddAlbum):

    def __init__(self, *args, **kwargs):
        super(DeleteAlbum, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
