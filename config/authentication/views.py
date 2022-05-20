from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings
from authentication import forms
from django.contrib import messages


#deconection
def logout_user(request):
    logout(request)
    return redirect('login')

#register
def signup_page(request):
    form = forms.UserRegisterForm()
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Utilisateur {username} créé avec succès. Maintenaint vous pouvez vous connecter')
            # return redirect(settings.LOGIN_REDIRECT_URL)
            return redirect('login')
        else:
            form = forms.UserRegisterForm()
    
    return render(request, 'authentication/signup.html', { 'form': form })