from django.shortcuts import render,redirect
from .models import Posts,Category,Author
from .forms import *
from django.db.models import Q


def delete_post(request,post_id):
    post = Posts.objects.get(id = post_id)
    post.delete()
    return redirect('post-list')

def post_list(request):
    list_of_post = Posts.objects.all()
    search = request.GET.get('search_value')
    if search:
        list_of_post = list_of_post.filter(
            Q(title__icontains=search) |
            Q(author__name__icontains=search) |
            Q(category__name__icontains=search)
        )
    context = {
        'post': list_of_post
    }
    return render(request,'new_blog/post_list.html',context)


def post_details(request, post_id):
    take_post = Posts.objects.get(id=post_id)
    context = {
        'single': take_post
    }
    return render(request,'new_blog/post_details.html',context)


def category_list(request):
    cat = Category.objects.all()
    context ={
        'cat_list': cat
    }
    return render(request,'new_blog/category.html',context)


def category_detail(request,cat_name):
    cat_det = Category.objects.get(name = cat_name)
    cat_post = Posts.objects.filter(category=cat_det)
    context = {
        'cat_po':cat_post
    }
    return render(request,'new_blog/category_detail.html',context)


def add_category(request):
    form = CategoryForm()
    context = {'form':form}
    cata_ne = request.GET.get('category')
    type_ne = request.GET.get('type')
    if cata_ne and type_ne:
        Category.objects.create(
            name = cata_ne,
            type = type_ne
        )
        return redirect('add-category')
    return render(request,'new_blog/add_category.html',context)


def author_add(request):
    form = AuthorForm()
    context = {'form':form}
    name_ne = request.GET.get('Name')
    mobile_ne = request.GET.get('Mobile_No')
    if name_ne and mobile_ne:
        Author.objects.create(
            name = name_ne,
            mobile_no = mobile_ne
        )
    return render(request,'new_blog/add_author.html',context)


def blog_add(request):
    form = BlogCreateForm()
    if request.method == 'POST':
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog-add')
    context = {'form': form}
    return render(request,'new_blog/add_blog.html',context)


def blog_search(request):
    forms = BlogSearch()
    context = {'form':forms}
    title_ne = request.GET.get('Search')
    if title_ne:
        dekhabo = Posts.objects.get(title__icontains = title_ne)
        dekhs = Posts.objects.filter(title=dekhabo)
        context = {'form':forms,'dekhabo':dekhs}
    return render(request,'new_blog/search.html',context)


