# Controladores de la aplicación
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Animatronic
from .forms import AnimatronicForm


# Lista pública de animatrónicos
def animatronic_list(request):
    animatronics = Animatronic.objects.all()
    return render(request, 'freddyapp/animatronic_list.html', {'animatronics': animatronics})

# Ver detalles (requiere login)
@login_required
def animatronic_view(request, id):
    animatronic = get_object_or_404(Animatronic, id=id)
    return render(request, 'freddyapp/animatronic_view.html', {'animatronic': animatronic})

# Crear animatrónico (permiso add)
@permission_required('freddyapp.add_animatronic')
def animatronic_new(request):
    if request.method == 'POST':
        form = AnimatronicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animatronic_list')
    else:
        form = AnimatronicForm()
    return render(request, 'freddyapp/animatronic_form.html', {'form': form, 'title': 'New animatronic'})

# Editar animatrónico (clase + permiso change)
class AnimatronicUpdate(PermissionRequiredMixin, UpdateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name = 'freddyapp/animatronic_form.html'
    pk_url_kwarg = 'id'
    permission_required = 'freddyapp.change_animatronic'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Edit animatronic'
        return ctx

    def get_success_url(self):
        return reverse_lazy('animatronic_list')

# Borrar animatrónico (clase + permiso delete)
class AnimatronicDelete(PermissionRequiredMixin, DeleteView):
    model = Animatronic
    template_name = 'freddyapp/animatronic_confirm_delete.html'
    pk_url_kwarg = 'id'
    permission_required = 'freddyapp.delete_animatronic'
    success_url = reverse_lazy('animatronic_list')

# Registro (añade al grupo Client)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='Client')
            user.groups.add(group)
            login(request, user)
            return redirect('animatronic_list')
    else:
        form = UserCreationForm()
    return render(request, 'freddyapp/register.html', {'form': form})

# Login con plantilla propia
class FreddyLoginView(LoginView):
    template_name = 'freddyapp/login.html'

# Logout estándar
class FreddyLogoutView(LogoutView):
    next_page = 'animatronic_list'

# Activar tema oscuro (cookie)
def set_dark_theme(request):
    response = redirect('animatronic_list')
    response.set_cookie('theme', 'dark')
    return response

# Borrar cookie de tema
def clear_theme(request):
    response = redirect('animatronic_list')
    response.delete_cookie('theme')
    return response
