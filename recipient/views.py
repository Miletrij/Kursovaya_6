from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from recipient.models import Recipient


class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    fields = ['email', 'name', 'description']
    success_url = reverse_lazy('recipient:list')


class RecipientUpdateView(UpdateView):
    model = Recipient
    fields = ['email', 'name', 'description']
    success_url = reverse_lazy('recipient:list')


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy('recipient:list')
