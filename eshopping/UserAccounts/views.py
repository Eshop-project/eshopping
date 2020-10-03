from django.urls import reverse_lazy
from django.views import generic

from .admin import UserCreationForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('store')
    # Try to force login and put user back in main page.
    template_name = 'signup.html'