from .forms import NameForm
from .df import detect_intent_texts
import json
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, HttpResponseRedirect

sn_id = 'ezPoz'
pr_id = 'newagent-nkwbgv'

@xframe_options_exempt
@require_http_methods(['GET'])
def index_view(request):
    form = NameForm()
    return render(request, "index.html", {'form':form})

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data

@xframe_options_exempt
@csrf_exempt
@require_http_methods(['POST'])
def bot(request):
    print(request.body)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["name"]
            return HttpResponse(query)

    print('Body', request.body)
    input_dict = convert(request.body)
    print(input_dict)
    input_text = json.loads(input_dict)['text']
    response = detect_intent_texts(pr_id, sn_id, input_text)
    return HttpResponse(response, status=200)






