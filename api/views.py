from django.http import (HttpRequest, JsonResponse)
from rest_framework.decorators import api_view


@api_view(['POST'])
def evaluate(request: HttpRequest) -> JsonResponse:
    """Evaluate the expression contained in request and return it as JSON."""

    return JsonResponse({})
