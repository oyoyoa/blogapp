from django.forms import ModelForm
from django.forms.fields import CharField
# from django.forms.widgets import TextInput

from blog.models import Post

class PostForm(ModelForm):
    content = CharField(
        max_length=140
    )

    class Meta:
        model = Post
        fields = ['content', 'image']

