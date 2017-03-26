from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Form for posting new comments."""

    class Meta:
        model = Comment
        fields = ('user', 'post', 'comment')