from django.shortcuts import render
from django.http import HttpResponse
# from django.utils.translation import gettext as _
from django.utils import translation

# Create your views here.
def index(request):
    # output = _("WelcomeMessage")
    # return HttpResponse(output)
    
    user_language = 'es'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SEESION_KEY] = user_language

    return render(request, 'index.html')