from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from . import models

POSTS_PER_PAGE = 5
COMMENTS_PER_PAGE = 5


class PostListView(generic.ListView):
    model = models.Post
    ordering = "-id"
    paginate_by = POSTS_PER_PAGE


class TagDetailView(generic.DetailView):
    model = models.Tag

    def get_object(self, queryset=None):
        return get_object_or_404(models.Tag, name=self.kwargs.get("name"))

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.object.posts.all(), POSTS_PER_PAGE)

        context = super(TagDetailView, self).get_context_data(**kwargs)
        pager = paginator.page(self.request.GET.get("page", 1))
        context["post_list"] = pager
        context["page_obj"] = pager

        return context


class PostDetailView(generic.DetailView):
    model = models.Post

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.object.approved_comments().all(), COMMENTS_PER_PAGE)

        context = super(PostDetailView, self).get_context_data(**kwargs)
        pager = paginator.page(self.request.GET.get("page", 1))
        context["comments"] = pager
        context["page_obj"] = pager

        return context


def licensing(request):
    return render(request, "blog/licensing.html")


def contact(request):
    return render(request, "blog/contact.html")


def post_comment(request):
    post = get_object_or_404(models.Post, id=request.POST["post_id"])
    comment = models.Comment()
    comment.post = post
    comment.author_name = request.POST["author_name"]
    comment.text = request.POST["text"]
    comment.save()

    return HttpResponseRedirect(post.url())
