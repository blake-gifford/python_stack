from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.display_show),
    path('shows/<int:show_id>/edit', views.edit_show), #edit_view
    path('shows/<int:show_id>/update', views.update_show), #edit_process
    path('shows/<int:show_id>/delete', views.delete_show)
]

