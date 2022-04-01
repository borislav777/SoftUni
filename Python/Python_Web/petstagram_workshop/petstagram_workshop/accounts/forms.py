from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from petstagram_workshop.accounts.models import Profile
from petstagram_workshop.main_app.models import PetPhoto


class CreateForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    description = forms.CharField(
        widget=forms.Textarea(),
    )

    email = forms.EmailField()
    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],

            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture')
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


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
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


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance
