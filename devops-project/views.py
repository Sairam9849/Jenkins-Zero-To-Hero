# optional top-level views if needed
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('/')
