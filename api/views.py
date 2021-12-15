from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import SyntaxValidator


class EvaluateView(CreateAPIView):
    serializer_class = SyntaxValidator

    def post(self, request):
        try:
            # result = eval(request.data.get('expression'))
            # TODO: calculate the right result
            result = 0
        except Exception as ex:
            return Response({'detail': str(ex)}, status=HTTP_400_BAD_REQUEST)

        return Response(
            {
                'result': result,
                'variables': request.data.get('variables')
            }
        )
