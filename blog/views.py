from django.shortcuts import render
from blog.models import Post, Author

# Визначення представлень, які обробляють бізнес-логіку та взаємодію з моделями для передачі даних до шаблонів

# функція представлення, яка буде відображати список постів
def post_list(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    context = {
        "posts_list": posts,
        "authors_list": authors,
    }
    return render(request=request, template_name="blog/post_list.html", context=context)

# функція представлення, яка буде відображати детальну сторінку конкретного посту
def get_post_by_id(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {
        "post": post,
    }
    return render(request=request, template_name="blog/post_details.html", context=context)


# функція представлення, яка буде відображати всі пости конкретного автора
def get_posts_by_author_id(request, author_id):
    author = Author.objects.get(id = author_id)
    posts = Post.objects.filter(id = author_id)
    context = {
        "author": author,
        "posts_list": posts,
    }
    return render(request=request, template_name="blog/authors_post.html", context=context)