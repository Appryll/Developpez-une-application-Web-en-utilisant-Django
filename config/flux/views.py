from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from review.models import Review
from flux.utils import get_user_follows, get_user_viewable_reviews, get_user_viewable_tickets, get_replied_tickets
from django.core.paginator import Paginator
from django.db.models import Value, CharField
from itertools import chain
from django.contrib.auth.models import User

@login_required
def flux(request):
    followed_users = get_user_follows(request.user)
    reviews = get_user_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = get_user_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    replied_tickets, replied_reviews = get_replied_tickets(tickets)
    posts_list = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    if posts_list:
        paginator = Paginator(posts_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    else:
        posts = None

    return render(request, 'flux/flux.html', context = {'posts': posts, 'replied_tickets': replied_tickets,
                                                        'replied_reviews': replied_reviews,
                                                        'title': 'Flux','followed_users': followed_users})

@login_required
def user_posts(request, pk=None):
    if pk:
        user = get_object_or_404(User, id=pk)
    else:
        user = request.user
    followed_users = get_user_follows(request.user)
    reviews = Review.objects.filter(user=user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user=user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    replied_tickets, replied_reviews = get_replied_tickets(tickets)
    posts_list = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    if posts_list:
        paginator = Paginator(posts_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        total_posts = paginator.count
    else:
        posts = None
        total_posts = 0

    return render(request, 'flux/my_posts.html', context = {'posts': posts,'title': f"{user.username}'s posts "
                                                f"({total_posts})",'r_tickets': replied_tickets,
                                                'r_reviews': replied_reviews, 'followed_users': followed_users})
