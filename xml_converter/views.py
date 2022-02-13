from django.http import JsonResponse
from django.shortcuts import render
from xml_converter import utils


def upload_page(request):
    if request.method == 'POST' and request.FILES.get('file'):
        result = {}
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            result = utils.xml_parse(uploaded_file.read())
        return JsonResponse(result)
    return render(request, "upload_page.html")
