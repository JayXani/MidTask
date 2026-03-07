from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .serializer import (
    ChecklistInputSerializer,
    ChecklistInputListSerializer,
    ChecklistOutputSerializer,
    ChecklistInputUpdateSerializer
)
from ..application.use_case.create_checklist_use_case import CreateChecklistsUseCase
from ..application.use_case.findall_checklist_use_case import FindAllChecklistsUseCase
from ..application.use_case.update_checklist_use_case import UpdateChecklistUseCase
from ..application.use_case.delete_checklists_use_case import DeleteChecklistUseCase
from setup.utils.messages.format_response import format_response

class CheckListView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
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


    def patch(self, request: Request, id: str):
        input_serializer = ChecklistInputUpdateSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        use_case = UpdateChecklistUseCase()
        checklist_updated = use_case.execute(input_serializer.validated_data, id, request.user.use_id)

        if(checklist_updated == 0): return Response(format_response(
            success=True,
            message="Anyone rows updated !",
            data={}
        ))

        return Response(format_response(
            success=True,
            message="Success ! Rows updated",
            data={}
        ))


    def delete(self, request: Request):
        input_serializer = ChecklistInputListSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        use_case = DeleteChecklistUseCase()
        checklist_deleted = use_case.execute(input_serializer.validated_data, request.user.use_id)

        if(not len(checklist_deleted) or (len(checklist_deleted) and checklist_deleted[0] <= 0)): return Response(format_response(
            success=True,
            message="Success ! You don't anyone register !",
            data={}
        ))

        return Response(format_response(
            success=True,
            data={},
            message="Success ! Data deleted."
        ))

class ManyCheckListView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        input_serializer = ChecklistInputListSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        use_case = FindAllChecklistsUseCase()
        checklists_founded = use_case.execute(input_serializer.validated_data, request.user.use_id)

        output_serializer = ChecklistOutputSerializer(instance=checklists_founded, many=True)
        return Response(format_response(
            success=True,
            message="Success ! Data returned",
            data=output_serializer.data
        ))
