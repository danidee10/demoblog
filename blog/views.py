from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category
from .forms import CommentForm

class PostListView(ListView):
    """Post list views."""

    model = Post
    template_name = 'blog/post_list.html'
    queryset = Post.published_posts.all()


class PostDetailView(DetailView):
    """Post detail view."""

    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        """Add comment form to the view context."""
        context = super().get_context_data(**kwargs)

        # add categories to context
        context['categories'] = Category.objects.all()

        # initialize form with post data
        obj = self.object
        context['form'] = CommentForm(
            initial={'post': obj.id, 'user': self.request.user}
            )

        return context


class NewComment(LoginRequiredMixin, FormView):
    """A post only view for new comments. for logged in users"""

    http_method_names = ['post']
    template_name = 'blog/post.html'
    form_class = CommentForm

    def form_valid(self, form):
        """Save the comment."""
        form.save()

        return super().form_valid(form)


    def get_success_url(self):
        """Redirect to current post on success."""
        post = self.request.POST.get('post')

        # get post slug
        post_slug = Post.objects.get(id=post).slug

        return reverse_lazy('blog:detail_view', kwargs={'slug': post_slug})

