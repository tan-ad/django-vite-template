from django.shortcuts import render
from django.http import HttpResponseServerError # Import for safety
import datetime

def index_view(request):
    """
    Serves the base HTML template which includes the Vue app.
    """
    print(f"--- index_view CALLED at {datetime.datetime.now()} for path: {request.path} ---")
    try:
        response = render(request, 'base.html')
        print(f"--- index_view RENDERED template successfully ---")
        return response
    except Exception as e:
        print(f"!!! ERROR rendering template in index_view: {e} !!!")
        return HttpResponseServerError(f"Error rendering base.html: {e}")
