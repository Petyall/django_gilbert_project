from django.views.generic.list import ListView
from forum.models import Post, PostCommentary
from django.views.generic.detail import DetailView
from forum.forms import UserCommentaryForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import ModelFormMixin, FormMixin
# Create your views here.

class HomeView(ListView):
    template_name = 'forum/index.html'
    model = Post

class Search(ListView):
    template_name = 'forum/index.html'
    model = Post

    def get_queryset(self, **kwargs):
        return Post.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'forum/post_detail.html'
    form_class = UserCommentaryForm


    def get_success_url(self):
        return reverse_lazy('forum:post_detail', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        post_id = self.kwargs.get('pk')
        context['comments'] = PostCommentary.objects.filter(post_id=post_id)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

        
    def form_valid(self, form):
        form.instance.author = self.request.user
        # post_id = self.kwargs.get('pk')
        # post = Post.objects.filter(id=post_id)
        # form.instance.post = Post.objects.filter(id=post_id)
        # print(Post.objects.get(pk=int(self.kwargs['pk'])))
        form.instance.post = Post.objects.get(pk=int(self.kwargs['pk']))
        form.save()
        return super(PostDetailView, self).form_valid(form)
        




#     def get_success_url(self):
#         return reverse_lazy('forum:post_detail', kwargs={'pk': self.object.id})

#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         post_id = self.kwargs.get('pk')
#         context['comments'] = PostCommentary.objects.filter(post_id=post_id)
#         context['form'] = UserCommentaryForm(initial={'post': self.object})
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         form.save()
#         return super(PostDetailView, self).form_valid(form)




# class PostDetailView(FormMixin, DetailView):
#     model = Post
#     template_name = 'forum/post_detail.html'
#     form_class = UserCommentaryForm

#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data()
#         post_id = self.kwargs.get('pk')
#         context['comments'] = PostCommentary.objects.filter(post_id=post_id)
#         return context

#     def get_success_url(self):
#         return reverse('post_detail', kwargs={'pk': self.object.pk})

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)