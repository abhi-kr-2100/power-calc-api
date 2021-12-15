from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def evaluate(request: HttpRequest) -> Response:
    """Evaluate the expression contained in request and return it as JSON."""

    return Response(request.data)
