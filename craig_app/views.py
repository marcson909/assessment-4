from django.shortcuts import render, redirect
from .models import Category, Post
from .forms import CategoryForm, PostForm, PostHomeForm
from django.views.generic.base import TemplateView



# homepage template with category context so that we can still see categories from the homepage
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        return context

# category and post helper functions
def get_category(category_id):
    return Category.objects.get(id=category_id)

def get_post(post_id):
    return Post.objects.get(id=post_id)

#cat list view
def category_list(request):
    all_categories = Category.objects.all()
    data = {'all_categories': all_categories}
    return render(request, 'category/category_list.html', data)

#new cat view
def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form, 'type_of_request': 'New'})

#cat detail view
def category_detail(request, category_id):
    category = get_category(category_id)

    #get the category posts so we can see them on detail view instead of needing to click a link

    posts = category.posts.all()

    #check to see if category has no parent and if no parent then list all posts from children categories
    if category.parent is None:
        all_children = category.children.all()
        data = {'category': category,'all_children': all_children, 'posts': posts}
        return render(request, 'category/category_detail.html', data)
    else:
        data = {'category': category, 'posts': posts}
        return render(request, 'category/category_detail.html', data)
    
#edit category view
def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form, 'type_of_request': 'Edit'})

#delete category view
def delete_category(request, category_id):
    if request.method == "POST":
        category = get_category(category_id)
        category.delete()
    return redirect('category_list')

#post detail view
def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    data = {'category': category, 'post': post}
    return render(request, 'post/post_detail.html', data)

#new post view
def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form, 'type_of_request': 'New'})

#edit post view
def edit_post(request, category_id, post_id):
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {'form': form, 'type_of_request': 'Edit'})

#delete post view
def delete_post(request, category_id, post_id):
    if request.method == "POST":
        post = get_post(post_id)
        post.delete()
    return redirect('category_detail', category_id=category_id)

#new post from home page view. since there is no category id on homepage we don't need one
#there is an option to select which category the post belongs to on this form page only
#the other new post view automatically selects the category the user was inside when selecting it
def new_post_home(request):
    if request.method == "POST":
        form = PostHomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            category = post.category
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
    else:
        form = PostHomeForm()
    return render(request, 'post/post_form.html', {'form': form, 'type_of_request': 'New'})





