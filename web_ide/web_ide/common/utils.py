from rest_framework.response import Response
from rest_framework.views import exception_handler

from web_ide.settings import DEBUG


def custom_exception_handler(exc, context):
    if DEBUG:
        raise

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return Response(data={'error': str(exc)}, status=500)
