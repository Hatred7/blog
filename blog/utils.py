from django.db.models import Count, Sum, F
from .models import Post, Comment


def filter_posts(request, query, posts):
    if query == 'my_posts':
        posts = posts.filter(
            author=request.user) if request.user.is_authenticated else posts

    if query == 'popular':
        posts = posts.annotate(likes_quantity=Count('likes'))\
            .order_by('-likes_quantity')[:10]
    if query == 'new_posts':
        posts = posts.order_by('-date')
    if query == 'favorite':
        posts = posts.filter(favorite=request.user)
    if query == 'liked_posts':
        posts = posts.filter(likes=request.user)
    if query == 'saved':
        posts = posts.filter(saved=request.user)
    if query == 'author_post':
        posts = posts.filter(author__pk=request.GET.get('user'))
    if query == 'comment':
        posts = posts.annotate(num_comment=Count(
            'comment')).order_by('-num_comment')
    if query == 'views':
        posts = posts.annotate(num_views=Count('views')).order_by('-num_views')
    if query == 'rate':
        posts = posts.annotate(rate=Count(
            'likes') + Count('comment') + Count('views')).order_by('-rate')

    return posts


def do_action(action, request):
    if action == 'favorite':
        post = Post.objects.get(pk=request.GET.get('pk'))
        if request.user not in post.favorite.all():
            post.favorite.add(request.user)
            return
        post.favorite.remove(request.user)


def add_saved(action, request):
    if action == 'saved':
        post = Post.objects.get(pk=request.GET.get('pk'))
        if request.user not in post.saved.all():
            post.saved.add(request.user)
            post.save()
            return
        post.saved.remove(request.user)


# def do_action(field_name, request, queryset):
#     post = Post.objects.get(pk=request.GET.get('pk'))

#     if request.user not in queryset.all():
#         getattr(post, field_name).add(request.user)
#         return
#     getattr(post, field_name).remove(request.user)
#     return

def filter_comments(request, query, comments):
    if query == 'new':
        comments = comments.order_by('-date')
    elif query == 'old':
        comments = comments.order_by('date')
    elif query == 'popular':
        comments = comments.annotate(likes_quantity=Count(
            'comment_likes')).order_by('-likes_quantity')
    else:
        comments = comments.filter(user=request.user)
    return comments
