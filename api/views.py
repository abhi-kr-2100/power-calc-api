from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from pcalc import VariablesTableType, Parser

from .serializers import SyntaxValidator


global_parser = Parser()


class EvaluateView(CreateAPIView):
    serializer_class = SyntaxValidator

    def post(self, request):
        expression = request.data.get('expression')
        variables_dict = request.data.get('variables') or dict()
        variables = VariablesTableType(variables_dict)

        try:
            result = global_parser.evaluate(expression, variables)
        except Exception as ex:
            return Response({'detail': str(ex)}, status=HTTP_400_BAD_REQUEST)

        return Response(
            {
                'result': result,
                'variables': variables
            }
        )
