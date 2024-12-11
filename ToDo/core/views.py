from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Proyecto, Tarea

# Vista de función para Home
def home(request):
    proyectos = Proyecto.objects.all()
    tareas = Tarea.objects.all()
    return render(request, 'home.html', {'proyectos': proyectos, 'tareas': tareas})

# Vistas para Proyecto y Tarea
class ProyectoCreateView(CreateView):
    model = Proyecto  
    template_name = 'create.html'
    fields = ['nombre', 'fecha_entrega', 'descripcion']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        tipo = self.request.POST.get('tipo')
        if tipo == 'Proyecto':
            form.instance = Proyecto(
                nombre=form.cleaned_data['nombre'],
                fecha_entrega=form.cleaned_data['fecha_entrega'],
                descripcion=form.cleaned_data['descripcion']
            )
        elif tipo == 'Tarea':
            form.instance = Tarea(
                nombre=form.cleaned_data['nombre'],
                fecha_entrega=form.cleaned_data['fecha_entrega'],
                descripcion=form.cleaned_data['descripcion']
            )
        return super().form_valid(form)

class ItemUpdateView(UpdateView):
    template_name = 'update.html'
    fields = ['nombre', 'fecha_entrega', 'descripcion']
    success_url = reverse_lazy('home')

    def get_object(self):
        item_type = self.kwargs['item_type']
        item_id = self.kwargs['pk']
        if item_type == 'proyecto':
            return get_object_or_404(Proyecto, pk=item_id)
        elif item_type == 'tarea':
            return get_object_or_404(Tarea, pk=item_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_type'] = self.kwargs['item_type']
        return context

# Función para eliminar ítems
def delete_item(request, item_type, item_id):
    if item_type == 'proyecto':
        item = get_object_or_404(Proyecto, pk=item_id)
    elif item_type == 'tarea':
        item = get_object_or_404(Tarea, pk=item_id)
    item.delete()
    return redirect('home')