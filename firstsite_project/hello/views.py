from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator  
from .models import *
# Create your views here.
def home(request):
    posts=Blog.objects.all().order_by('id')
    paginator = Paginator(posts,3) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request, 'home.html', {'page_posts': page_posts})

def new(request):
    return render (request, 'new.html')

def postcreate(request):
    post=Blog()
    post.title=request.POST ['title']
    post.body=request.POST ['body']
    post.save()
    return redirect ('home')

def detail(request,post_id):
    onepost = get_object_or_404(Blog, pk=post_id)
    comments = onepost.blogcomment_set.all()
    return render(request, 'detail.html',{'onepost': onepost, 'comments': comments})

def postedit(request,post_id):
    onepost = get_object_or_404(Blog,pk=post_id)
    return render(request,'postedit.html',{'onepost':onepost})
def postupdate(request,post_id):
    onepost = get_object_or_404 (Blog, pk = post_id)
    onepost.title = request.POST['title']
    onepost.body = request.POST['body']
    onepost.save()
    return redirect('/detail/'+str(post_id))
def postdelete(request,post_id):
    onepost= get_object_or_404(Blog, pk=post_id)
    onepost.delete()
    return redirect ('home')

def commentcreate(request,post_id):
    if (request.method == 'POST'):
        post = get_object_or_404(Blog,id = post_id)
        post.blogcomment_set.create(title = request.POST['comment_content'])
    return redirect('/blog/detail/'+ str (post_id))

def commentdelete(request,post_id,comment_id):
    comment = get_object_or_404(BlogComment, id = comment_id, blog_id=post_id)
    comment.delete()
    return redirect('/blog/detail/'+ str (post_id))

