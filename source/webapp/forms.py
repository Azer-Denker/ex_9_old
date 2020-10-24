from django import forms
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

from webapp.models import Photo, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description', 'author_name']


class XDatepickerWidget(forms.TextInput):
    template_name = 'widgets/xdatepicker_widget.html'


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
