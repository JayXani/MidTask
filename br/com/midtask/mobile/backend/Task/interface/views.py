from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..infra.messages import format_response

class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        try:
            return Response({})
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to create a task",
                err=e
            ))