# Файл для оголошення URL маршрутів проекту, вказує Django, які представлення використовувати для обробки різних HTTP запитів
from django.urls import path # дозволить просто формувати шляхи до наших view
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_list, name="post_list"),
    path("<int:post_id>/", blog_views.get_post_by_id, name="post_details"),
    path("author/<int:author_id>/", blog_views.get_posts_by_author_id, name="authors_post"),
]
