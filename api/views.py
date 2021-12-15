from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def evaluate(request: HttpRequest) -> Response:
    """Evaluate the expression contained in request and return it as JSON."""

    if request.content_type != 'application/json':
        return Response(
            {'detail': 'Unsupported content type'},
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        )

    if 'expression' not in request.data:
        return Response(
            {'detail': 'No expression in payload'},
            status.HTTP_400_BAD_REQUEST
        )

    return Response(request.data)
