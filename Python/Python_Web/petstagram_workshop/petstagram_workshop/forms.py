from django import forms

from petstagram_workshop.main_app.models import Profile, Pet, PetPhoto




class CreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),
            'picture': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL'
                }
            )
        }


# class AddPet(forms.Form):
#     CAT = "Cat"
#     DOG = "Dog"
#     BUNNY = "Bunny"
#     PARROT = "Parrot"
#     FISH = "Fish"
#     OTHER = "Other"
#     TYPE = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
#
#     pet_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter pet name'
#             }
#         )
#
#     )
#     type = forms.ChoiceField(
#
#         choices=TYPE,
#
#         widget=forms.Select(
#
#             attrs={
#                 'class': 'form-control',
#                 'selected': 'HKJHKH',
#
#             }
#         ),
#
#     )
#     day_of_birth = forms.DateTimeField(
#         widget=forms.SelectDateWidget(
#             years=[x for x in range(1920, 2023)],
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': '----'
#
#             }
#
#         )
#     )

class AddPet(forms.ModelForm):
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
            'user_profile': forms.HiddenInput()
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


class EditProfile(CreateForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',

                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'picture': forms.URLInput(
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
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                    'selected': 'Do not show',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            )
        }
