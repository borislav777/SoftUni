from django import forms

from recipes.web.models import Recipe


class CreateRecipe(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateRecipe, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Recipe
        fields = '__all__'



class EditRecipe(CreateRecipe):
    pass


class DeleteRecipe(CreateRecipe):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipe, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
