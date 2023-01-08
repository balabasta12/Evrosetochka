from django import forms


class AddPostForm(forms.Form):
    token = forms.CharField(max_length=255)
