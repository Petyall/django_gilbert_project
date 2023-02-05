from django.contrib.auth.views import LoginView
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from users.models import User

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('users:login')


class UserProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    model = User

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))