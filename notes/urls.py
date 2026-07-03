
from django.urls import path
from . import views
urlpatterns = [
    path('',views.notes, name='testing_notes'),
    path('notes/<int:id>/', views.notes_detail, name='notes_detail'),
    path('forms/',views.forms_concept,name='forms_concept')
]


