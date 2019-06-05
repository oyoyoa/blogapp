from django.views.generic import TemplateView
from blog.models import Post
# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post_list'] = Post.objects.all().order_by('-created_at')[:5]
        return context

