from rest_framework import serializers


class SyntaxValidator(serializers.Serializer):
    expression = serializers.CharField(max_length=200)
    variables = serializers.DictField(child=serializers.FloatField())
