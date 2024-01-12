from django.contrib.auth import logout
from django.shortcuts import redirect, render, reverse
from django.views.generic import UpdateView, DetailView
from .models import Profile, User
from .forms import ProfileEditForm, ProfileUpdateForm


class EditProfileUser(DetailView):
    model = User
    form_class = ProfileEditForm
    slug_url_kwarg = 'username'
    slug_field = 'username'
    context_object_name = 'user'
    template_name = 'user_profile/edit_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.kwargs['username']

        return context


def profile_update(request):
    if request.method == 'POST':
        u_form = ProfileEditForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(reverse('edit_profile', kwargs={'username': request.user.username}))

    else:
        u_form = ProfileEditForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_profile/update_profile.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
