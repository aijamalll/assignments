from django.urls import path
from . import views

urlpatterns = [
    path('cinema/', views.Details_view.as_view(), name='cinema'),
    path('cinema/<int:id>', views.Show_details_view.as_view(), name='show'),
    path('notes/', views.View_user_notes.as_view(), name='notes'),
    path('notes/<int:id>/update_note/',
        views.View_update_note.as_view(), name='update'),
    path('notes/<int:id>/delete_note/',
        views.View_delete_note.as_view(), name='delete'),
    path('notes/add_note/', views.View_create_note.as_view(), name='add'),
]