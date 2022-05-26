from django.shortcuts import render, redirect
from review.forms import ReviewForm
from ticket.forms import TicketForm
from review import forms, models
from django.contrib.auth.decorators import login_required
from review.models import Review
from ticket.models import Ticket

@login_required
def review_create(request):
    if request.method == 'POST':
        rev_form = ReviewForm(request.POST)
        tic_form = TicketForm(request.POST, request.FILES)

        if rev_form.is_valid() and tic_form.is_valid():
           
            ticket = tic_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            Review.objects.create(
                ticket=Ticket.objects.get(pk=ticket.id),
                rating=rev_form.cleaned_data['rating'],
                user=request.user,
                headline=rev_form.cleaned_data['headline'],
                body=rev_form.cleaned_data['body']
            )

            return redirect('flux')
    else:
        rev_form = ReviewForm()
        tic_form = TicketForm()
    
    return render(request,'review/new_review.html', {'tic_form':tic_form,'rev_form':rev_form})


@login_required
def flux_rev(request):
    reviews = models.Review.objects.all()
    return render(request, 
            'flux/flux.html', 
            {'reviews': reviews})
