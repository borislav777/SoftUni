from django import forms

from online_library.web.models import Profile, Book


class CreateProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProfile, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class EditProfile(CreateProfile):
    pass


class DeleteProfile(CreateProfile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance


class CreateBook(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateBook, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            )
        }


class EditBook(CreateBook, forms.ModelForm):
    pass


class DeleteBook(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = ()
