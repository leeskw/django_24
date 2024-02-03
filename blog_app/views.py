from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CommentForm, CreateBlogForm
from .models import Blog, Category, Comment


# path('', views.index , name='index'),
def index(request):
    keyword = request.GET.get("search")
    msg=None
    paginator = None
    if keyword:
        blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(body__icontains=keyword) | 
                                    Q(category__title__icontains=keyword))
        
        if blogs.exists():
            paginator = Paginator(blogs, 4)
            blogs = paginator.page(1)
        
        else:
            msg = "There is no article with the keyword"
            
    else:
        blogs = Blog.objects.filter(featured=False)
        paginator = Paginator(blogs, 4)
        page = request.GET.get("page")
        
        try:
            blogs = paginator.page(page)
            
        except PageNotAnInteger:
            blogs = paginator.page(1)
        
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        
    categories = Category.objects.all()
    context = {"blogs":blogs, "msg":msg, "paginator": paginator, "cats": categories}
    return render(request, "blog_app/index.html", context)


# path('article/<slug:slug>/', views.detail , name='detail'),
def detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    related_blogs = Blog.objects.filter(category__id=blog.category.id).exclude(id=blog.id)[:4]
    
    comments = Comment.objects.filter(blog=blog)
    form = CommentForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.user = request.user 
                comment.save()
                return redirect("detail", slug=blog.slug)
    context = {
      'blog': blog, 
      "form": form, 
      "comments": comments, 
      "r_blogs": related_blogs
    }
    return render(request, "blog_app/detail.html", context)


# path('create/article/', views.BlogCreateView.as_view(), name='create-article'), 
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog    
    template_name = 'blog_app/create.html'
    fields = ["title", "body", "thumbnail", "category"]
    success_url = reverse_lazy('profile')
    success_message = 'Article created successfully!'
    
    def get_form(self):
      form = super().get_form()
      
      
      for field_name in form.fields:
        if field_name == 'category':
          form.fields[field_name].widget.attrs['class'] = 'form-select'
        else: 
          form.fields[field_name].widget.attrs['class'] = 'form-control' 
        
        if field_name == 'thumbnail':
          form.fields[field_name].widget.attrs['placeholder'] = 'Add image'    
        else:        
          form.fields[field_name].widget.attrs['placeholder'] = 'Enter ' + field_name           
    
      return form
    
    def form_valid(self, form):
      form.instance.user = self.request.user

    
# path('update/article/<slug:slug>/', views.BlogUpdateView.as_view(), name='update-article'), 
class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog    
    template_name = 'blog_app/create.html'
    fields = ["title", "body", "thumbnail", "category"]
    success_url = reverse_lazy('profile')
    success_message = 'Article updated successfully!'
    
    def get_form(self):
      form = super().get_form()
      
      for field_name in form.fields:
        if field_name == 'category':
          form.fields[field_name].widget.attrs['class'] = 'form-select'
          
        form.fields[field_name].widget.attrs['class'] = 'form-control' 
        
        if field_name == 'thumbnail':
          form.fields[field_name].widget.attrs['placeholder'] = 'Add image'          
        form.fields[field_name].widget.attrs['placeholder'] = 'Enter ' + field_name           
    
      return form
    
    def form_valid(self, form):
      form.instance.user = self.request.user
      
      return super().form_valid(form)
    

# path('delete/article/<slug:slug>/', views.BlogDeleteView.as_view(), name='delete-article'), 
class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'core/profile.html'
    success_url = reverse_lazy('profile')
    success_message = 'Article deleted successfully!'


# # path('create/article', views.create_article, name='create-article'), 
# @login_required(login_url="signin")
# def create_article(request):
#     form=CreateBlogForm()
#     if request.method == 'POST':
#         form = CreateBlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.slug = slugify(request.POST["title"])
#             blog.user=request.user
#             blog.save()
#             messages.success(request, "Article created successfully!")
#             return redirect("profile")
#     context = {"form": form}
#     return render(request, "blog_app/create.html", context)    
    
    
# @login_required(login_url="signin")
# def update_article(request, slug):
#     update = True
#     blog = Blog.objects.get(slug=slug)
#     form=CreateBlogForm(instance=blog)
#     if request.method == 'POST':
#         form = CreateBlogForm(request.POST, request.FILES, instance=blog)
#         blog = form.save(commit=False)
#         blog.slug=slugify(request.POST["title"])
#         blog.save()
#         messages.success(request, "Article updated successfully")
#         return redirect("profile")
#     context={"update":update, "form":form}
#     return render(request, "blog_app/create.html", context)    


# @login_required(login_url="signin")
# def delete_article(request, slug):
#     blog = Blog.objects.get(slug=slug)
#     blogs = Blog.objects.filter(user=request.user)
#     delete_article = True
#     if request.method == 'POST':
#         blog.delete()
#         messages.success(request, "Article deleted successfully")
#         return redirect("profile")
#     context = {"blog": blog, "del":delete_article, "blogs": blogs}
#     return render(request, "core/profile.html", context)
