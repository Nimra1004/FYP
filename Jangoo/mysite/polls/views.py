
from django.views.generic.base import TemplateView
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
# In[1]
from . import predict
from . import content
from . import Generate
from . import Main
from . import nlu
from . import nlg




class Home(TemplateView):

    template_name = 'Home.html'


from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
@csrf_exempt

@csrf_protect
def get_name(request):
    reply = Main.sadia
    print(reply)
    console.log(reply)
    # if this is a POST request we need to process the form data
    form = NameForm()
    if request.method == 'POST':
        form = NameForm(request.POST)
        form.reply = Main.sadia
        text = request.POST["textfield"]

            # In[91]
            #form.reply = "hello"
        context = {
            'form': form,
            'reply': reply
        }
    return render(request, 'Home.html', context)





