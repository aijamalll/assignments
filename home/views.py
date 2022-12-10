from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from . import models, forms


# получение информации(GET)

class Details_view(generic.ListView):
    template_name = 'home.html'
    queryset = models.Cinema.objects.all()

    def get_queryset(self):
        return models.Cinema.objects.all()


# GET ID

class Show_details_view(generic.DetailView):
    template_name = 'wash.html'

    def get_object(self, *kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.Cinema, id=id)

class View_user_notes(generic.ListView):
    template_name = 'create.html'
    queryset = models.Model_notes_of_user.objects.all()

    def get_queryset(self):
        return models.Model_notes_of_user.objects.all()

class View_create_note(generic.CreateView):
    template_name = 'add_note.html'
    form_class = forms.Form_notes
    queryset = models.Model_notes_of_user.objects.all()
    success_url = '/notes/'

    def form_valid(self, form):
        return super(View_create_note, self).form_valid(form=form)

class View_update_note(generic.UpdateView):
    template_name = 'update_note.html'
    form_class = forms.Form_notes
    success_url = '/notes/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(models.Model_notes_of_user, id=note_id)

    def form_valid(self, form):
        return super(View_update_note, self).form_valid(form=form)

class View_delete_note(generic.DeleteView):
    template_name = 'delete_note.html'
    success_url = '/notes/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(models.Model_notes_of_user, id=note_id)