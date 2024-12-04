from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='blogmanager/index.html'), name='home'),
    path('create-blog/', views.CreateBlog, name='create_blog'),
]