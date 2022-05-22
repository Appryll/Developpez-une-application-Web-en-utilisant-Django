from django.shortcuts import render, redirect, get_object_or_404
from ticket.forms import TicketForm
from ticket import forms, models
from django.contrib.auth.decorators import login_required


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    else:
        form = TicketForm()
    
    return render(request, 
            'ticket/new_ticket.html', 
            {'form': form})


# @login_required
# def view_ticket(request, pk):
#     ticket = get_object_or_404(models.Ticket, id=pk)
#     return render(request, 
#             'ticket/view_ticket.html', 
#             {'ticket': ticket})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_ticket = forms.TicketForm(instance=ticket)
    delete_ticket = forms.DeleteTicketForm()
    
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_ticket = forms.TicketForm(request.POST, request.FILES, instance=ticket)
            if edit_ticket.is_valid():
                edit_ticket.save()
                return redirect('flux')
        if 'delete_ticket' in request.POST:
            delete_ticket = forms.DeleteTicketForm(request.POST)
            if delete_ticket.is_valid():
                ticket.delete()
                return redirect('flux')
    return render(request, 
    'ticket/edit_ticket.html', 
    context={'edit_ticket': edit_ticket,'delete_ticket': delete_ticket})


@login_required
def flux(request):
    tickets = models.Ticket.objects.all()
    return render(request, 
            'flux/flux.html', 
            {'tickets': tickets})