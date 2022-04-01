from django import forms


from petstagram_workshop.main_app.models import  Pet, PetPhoto




class AddPet(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        pet = super().save(commit=False)

        pet.user = self.user
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        exclude = ('user',)
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'name': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name'
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',

                }

            ),
            'date_of_birth': forms.SelectDateWidget(

                years=[x for x in range(1920, 2023)],
                attrs={
                    'class': 'form-control',

                }
            ),

        }


class EditPet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'name': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name'
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',

                }

            ),
            'date_of_birth': forms.SelectDateWidget(

                years=[x for x in range(1920, 2023)],
                attrs={
                    'class': 'form-control',

                }
            ),
            'user': forms.HiddenInput()
        }


class AddPhoto(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets',
        }
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    'class': 'form-control-file',

                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,

                }
            ),
            'tagged_pets': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                }
            )
        }


class EditPhoto(AddPhoto):
    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,

                }
            ),
            'tagged_pets': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                }

            )
        }


class DeletePet(AddPet):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'name': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'disabled': 'disabled',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'disabled': 'disabled',

                }

            ),
            'date_of_birth': forms.SelectDateWidget(
                years=[x for x in range(1920, 2023)],
                attrs={
                    'class': 'form-control',
                    'disabled': 'disabled',

                }
            ),

        }



