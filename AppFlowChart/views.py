from django.http import HttpResponse
from django.template import loader


def index(request):
    # getting our template
    template = loader.get_template('AppFlowChart/index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

# def index(request):
#     return HttpResponse("Hello, world. You're at the flowchart index.")
