from django.http import HttpRequest
from django.http.response import HttpResponseNotAllowed, JsonResponse


def evaluate(request: HttpRequest) -> JsonResponse:
    """Evaluate the expression contained in request and return it as JSON."""

    if request.method != 'POST':
        return HttpResponseNotAllowed('Only POST allowed')
    
    return JsonResponse({})
