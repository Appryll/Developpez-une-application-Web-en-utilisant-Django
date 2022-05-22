from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket


@login_required
def flux(request):
    tickets = Ticket.objects.all()
    return render(request, 'flux/flux.html', context={'tickets': tickets})