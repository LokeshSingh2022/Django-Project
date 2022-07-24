from django.shortcuts import render
from .forms import State_details_form

# Create your views here:-
def index(request):
    form = State_details_form()

    if request.method == 'POST':
        form = State_details_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'index.html', context)