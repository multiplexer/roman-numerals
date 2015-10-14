from django.shortcuts import render
from .romannumerals import *
from django.contrib import messages

# Decided not to implement a form class because of a lack of validating model.  Used the messaging system
# instead to communicate up flash messages for the error.

def index(request):

    if request.method == "POST":

        num = request.POST.get('decimal')

        # Check if is an int
        if not num.isdigit() or (int(num) < 1 and int(num) > 3999):
            messages.error(request, 'Must be a number between 1 and 3999.')
            return render(request, 'index.html')

        # Run the conversion
        try:
            val = convert_d_to_r(int(request.POST.get('decimal')))
            return render(request, 'index.html', {'value': val})
        except ValueError:
            return render(request, 'index.html')

    else:
        return render(request, 'index.html')