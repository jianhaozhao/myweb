from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
# Create your views here.

def test(request):
    result={"aa":"bb"}
    return HttpResponse(json.dumps(result), content_type="application/json")