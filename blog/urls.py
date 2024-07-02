from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, BlogListView

app_name = BlogConfig.name
urlpatterns = [
    path("list/", BlogListView.as_view(), name="list"),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_view'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
