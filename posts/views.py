from django.shortcuts import render, redirect
from django.views import View
from posts.models import Post

# Create your views here.
class PostList(View):
    template_name = "posts/post_list.html"

    def get(self, request):
        post_list = Post.objects.all()
        context = {
            'post_list':post_list
        }
        return render(request, self.template_name, context)
    
class PostCreate(View):
    template_name = "posts/post_form.html"
    success_url = "posts:post_list"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        Post.objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text')
        )
        return redirect(self.success_url)

