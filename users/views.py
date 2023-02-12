from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserReceiptForm
from users.models import User, UsersReceipts


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
    

class UserReceiptView(CreateView):
    template_name = 'users/user_receipt.html'
    form_class = UserReceiptForm
    model = UsersReceipts
    success_url = reverse_lazy('users:user_receipt')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserReceiptView, self).get_context_data()
        context['is_user_have_post'] = True if UsersReceipts.objects.filter(author=self.request.user) else False
        return context
