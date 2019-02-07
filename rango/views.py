from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# First view, from 3.5
def index(request):
    # Construct a context dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

# 3.6 exercise
def about(request):
    return render(request, 'rango/about.html')