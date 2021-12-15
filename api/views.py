from django.http import (HttpRequest, HttpResponse, JsonResponse,
    HttpResponseNotAllowed)


def evaluate(request: HttpRequest):
    """Evaluate the expression contained in request and return it as JSON."""

    if request.method != 'POST':
        return HttpResponseNotAllowed('Only POST allowed')
    
    return JsonResponse({})
