from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


def not_valid_exception(serializer):
    return Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)
