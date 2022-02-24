from django import forms

from notes.web.models import Profile, Note


class CreateProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProfile, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Link to Profile Image',
        }


class DeleteProfile(CreateProfile):

    def save(self, commit=True):
        self.instance.delete()
        Note.objects.all().delete()

    class Meta:
        model = Profile
        fields = ()


class CreateNote(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateNote, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Note
        fields = '__all__'


class EditNote(CreateNote):
    pass


class DeleteNote(CreateNote):
    def __init__(self, *args, **kwargs):
        super(DeleteNote, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
