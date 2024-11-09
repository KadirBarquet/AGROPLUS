from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class AdminLoginView(LoginView):
    template_name = 'security/auth/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        messages.success(self.request, _('Inicio de sesión exitoso'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Nombre de usuario o contraseña incorrectos'))
        return super().form_invalid(form)
    
def Admin_Logout(request):
    logout(request)
    return redirect('catalog:home')
