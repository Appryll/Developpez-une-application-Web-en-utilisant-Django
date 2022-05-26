"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# service des fichiers statiques en développement
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

import authentication.views
import flux.views
import ticket.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #conection
    path('', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    #register
    path('signup/', authentication.views.signup_page, name='signup'),
    #deconection
    path('logout/', authentication.views.logout_user, name='logout'),
    #pag ppal
    path('flux/', flux.views.flux, name='flux'),
    path('ticket-new/', ticket.views.ticket_create, name='ticket-new'),
    # path('ticket/<int:pk>', ticket.views.view_ticket, name='ticket-views')
    path('ticket/<int:ticket_id>/edit', ticket.views.edit_ticket, name='edit-ticket'),
    path('abonnements/', authentication.views.follow, name='abonnements'),
    path('subscriptions/confirm_unsub/<int:pk>/', authentication.views.UnsubscribeView.as_view(), name='confirm-unsub'),
    # path('unfollow/<str:username>/', authentication.views.unfollow, name='unfollow'),

    #review
    path('review/', review.views.review_create, name='review-new'),
] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
