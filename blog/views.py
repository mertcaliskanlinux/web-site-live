from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from django.urls import reverse
from blog.models import Post,Comment
from hitcount.views import HitCountDetailView
from blog.forms import CommentForm

def blog(request):
    context = {}
    return render(request,'blog/blog.html',context)



class PostDetailView(HitCountDetailView):
    model = Post
    template_name = "blog/post.html"
    slug_field = "slug"
    count_hit = True
    
    form = CommentForm
    
    def post(self,request,*ars,**kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            print(form.instance.user)
            form.instance.post = post
            form.save()
            
            return redirect(reverse("post",kwargs={
                'slug':post.slug,
            }))    
            
    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'form':self.form,
                'post_comments':post_comments
            }
        )
        
        return context