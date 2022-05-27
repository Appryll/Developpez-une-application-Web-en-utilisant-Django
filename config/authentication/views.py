from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from authentication import forms
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Relationship

#register
def signup_page(request):
    form = forms.UserRegisterForm()
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Utilisateur {username} créé avec succès. Maintenaint vous pouvez vous '
                                      f'connecter')
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            form = forms.UserRegisterForm()
    return render(request, 'authentication/signup.html', { 'form': form })

#deconection
def logout_user(request):
    logout(request)
    return redirect('login')

def follow(request):
    current_user = request.user
    user_serch = request.GET.get("serch")
    if user_serch:
        to_user = User.objects.get(username=user_serch)
        to_user_id = to_user
        rel = Relationship(from_user=current_user, to_user=to_user_id)
        rel.save()

    user_follows = Relationship.objects.filter(from_user=request.user).order_by('to_user')
    followed_by = Relationship.objects.filter(to_user=request.user).order_by('from_user')

    return render(request, 'authentication/follow_users_form.html', {'user_follows': user_follows,
                                                                     'followed_by': followed_by,})

class UnsubscribeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Relationship
    success_url = '/abonnements'
    context_object_name = 'unsub'

    def test_func(self):
        unsub = self.get_object()
        if self.request.user == unsub.from_user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, f'You have stopped following {self.get_object().followed_user}.')
        return super(UnsubscribeView, self).delete(request, *args, **kwargs)
