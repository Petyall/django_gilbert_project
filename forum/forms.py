from forum.models import PostCommentary
from django import forms


class UserCommentaryForm(forms.ModelForm):
    description = forms.Textarea()

    class Meta:
        model = PostCommentary
        fields = ('description',)