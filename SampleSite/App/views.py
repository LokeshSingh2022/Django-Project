from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def helloworld(request):
    logging.error('Hello world in the log...')
    print('Hello world in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/LokeshSingh2022/Django-Project.git</a></p>
    </body></html>"""
    return HttpResponse(response)