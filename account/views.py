from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.views import generic
from account.forms import SignUpForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })

@login_required
def profile_update(request):
    user = request.user
    form = ProfileUpdateForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("POST sending you back HOME")
            return HttpResponseRedirect(reverse('articles:home'))
        else:
            print("error")
    else:
        print("GET profile.html")
    context = {
        "profile_updateform":form,
    }
    return render(request, 'account/profile_update.html', context)