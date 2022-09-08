from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.admin import site

# Create your views here.
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Welcome to WordStore</h1>
            <p>The current time is {now}</p>
            <a href="/admin">The word store </a>
        </body>
    </html>
    '''
    return HttpResponse(html)