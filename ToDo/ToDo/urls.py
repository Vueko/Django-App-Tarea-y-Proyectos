from django.contrib import admin
from django.urls import path
from core.views import home, ProyectoCreateView, ItemUpdateView, delete_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', ProyectoCreateView.as_view(), name='create'),
    path('update/<str:item_type>/<int:pk>/', ItemUpdateView.as_view(), name='update_item'),
    path('delete/<str:item_type>/<int:item_id>/', delete_item, name='delete'),
]
