from django.shortcuts import render, redirect, get_object_or_404
from ticket.forms import TicketForm
from ticket import forms, models
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from ticket.models import Ticket

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES.get('image', None)
            Ticket.objects.create(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description'],
                image=image
            )
            return redirect('flux')
    else:
        form = TicketForm()
    
    return render(request, 'ticket/new_ticket.html', {'form': form,'title': 'CREATE TICKET', 'anonce': 'Créer un ticket'})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if ticket.user != request.user:
        raise PermissionDenied()
    
    if request.method == 'POST':
        edit_ticket = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_ticket.is_valid():
            edit_ticket.save()
            return redirect('flux')
    else:
        edit_ticket = forms.TicketForm(instance=ticket) 
    return render(request, 'ticket/new_ticket.html', {'form': edit_ticket, 'title': 'MODIFIER VOTRE TICKET', 'anonce': 'Modifier votre ticket'})

class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Ticket
    success_url = '/my_posts/'
    context_object_name = 'post'

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        return super(TicketDeleteView, self).delete(request, *args, **kwargs)
