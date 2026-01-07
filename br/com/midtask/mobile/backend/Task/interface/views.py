from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..infra.messages import format_response
from .serializer import (
    TaskInputSerializer,
    TaskOutputSerializer
)
from ..application.use_cases.CreateTaskUseCase import CreateTaskUseCase

class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        try:
            serializer = TaskInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            use_case = CreateTaskUseCase()
            task_created = use_case.execute(serializer.validated_data, request.user.use_id)

            output_serializer = TaskOutputSerializer(instance=task_created, many=True)
            return Response(format_response(
                success=True,
                message="Success ! Task Created.",
                data=output_serializer.data
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to create a task",
                err=e
            ))