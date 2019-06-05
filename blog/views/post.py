from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from blog.models import Post
from blog.forms import PostForm

class PostFormView(FormView):
    template_name = 'blog/post.html'
    form_class = PostForm
    success_url = '/'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
