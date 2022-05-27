from django.shortcuts import render, redirect, get_object_or_404
from review.forms import ReviewForm
from ticket.forms import TicketForm
from review import forms, models
from django.contrib.auth.decorators import login_required
from review.models import Review
from ticket.models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import DeleteView
from django.core.exceptions import PermissionDenied

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
    
    return render(request,'review/new_review.html', {'tic_form':tic_form,'rev_form':rev_form, 
    'title': 'CREATE REVIEW', 'anonce': 'Créer une review'})

@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, id=pk)
    if review.user != request.user:
        raise PermissionDenied()

    if request.method == 'POST':
        r_form = ReviewForm(request.POST, instance=review)
        if r_form.is_valid():
            r_form.save()
            return redirect('flux')

    else:
        r_form = ReviewForm(instance=review)

    return render(request, 'review/new_review.html', {'rev_form': r_form,'post': review.ticket,
        'title': 'MODIFIER VOTRE REVIEW', 'anonce': 'Modifier votre Review'})

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/my_posts/'
    context_object_name = 'post'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        return super(ReviewDeleteView, self).delete(request, *args, **kwargs)

@login_required
def review_response(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)

    if request.method == 'POST':
        r_form = ReviewForm(request.POST)
        if r_form.is_valid():
            Review.objects.create(
                ticket=ticket,
                user=request.user,
                headline=request.POST['headline'],
                rating=request.POST['rating'],
                body=request.POST['body']
            )
            return redirect('flux')
    else:
        r_form = ReviewForm()

    return render(request, 'review/review_form.html', {'r_form': r_form,'post': ticket,'title': 'Response Critique'})
