import os

from django import forms

from expenses.web.models import Profile, Expense


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')

        widgets = {
            'profile_image': forms.FileInput(
                attrs={
                    'class': 'form-file',
                }
            ),
        }


class EditProfile(CreateProfile):
    pass


class DeleteProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        img_url = self.instance.profile_image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(img_url)
        return self.instance


class CreateExpense(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image',
        }


class EditExpense(CreateExpense):
    pass


class DeleteExpense(CreateExpense):
    def __init__(self, *args, **kwargs):
        super(DeleteExpense, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
