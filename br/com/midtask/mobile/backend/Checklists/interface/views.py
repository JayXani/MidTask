from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .serializer import (
    ChecklistInputSerializer,
    ChecklistOutputSerializer
)
from ..application.use_case.create_checklist_use_case import CreateChecklistsUseCase
from ..infra.messages import format_response

class CheckListView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        try:
            input_serializer = ChecklistInputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            use_case = CreateChecklistsUseCase()
            checklists_created = use_case.execute(input_serializer.validated_data, request.user.use_id)

            output_serializer = ChecklistOutputSerializer(instance=checklists_created, many=True)
            return Response(format_response(
                success=True,
                message="Success ! Checklist created.",
                data=output_serializer.data
            ))

        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to create a task",
                err=e
            ))