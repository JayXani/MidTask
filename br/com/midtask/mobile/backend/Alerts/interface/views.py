from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from setup.utils.messages.format_response import format_response
from .serializer import (
    AlertInputSerializer,
    AlertInputUpdateSerializer,
    AlertsListInputSerializer,
    OutputSerializer
)
from ..application.use_cases.create_alerts_use_case import CreateAlertsUseCase
from ..application.use_cases.find_unique_alert_use_case import FindUniqueAlertUseCase
from ..application.use_cases.findall_alerts_use_case import FindAllAlertsUseCase
from ..application.use_cases.update_alerts_use_case import UpdateAlertsUseCase
from ..application.use_cases.delete_alerts_use_case import DeleteAlertsUseCase

# Create your views here.
class AlertsView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        serializer = AlertInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = CreateAlertsUseCase()
        alert_created = use_case.execute(serializer.validated_data, request.user.use_id)
    
        output_serializer = OutputSerializer(instance=alert_created, many=True)
        return Response(format_response(
            success=True,
            data=output_serializer.data,
            message="Success ! Alert inserted."
        ))

    def get(self, request:Request, id: str):
        use_case = FindUniqueAlertUseCase()
        alerts_founded = use_case.execute(id, request.user.use_id)
        output_serializer = OutputSerializer(instance=alerts_founded, many=True)

        return Response(format_response(
            success=True,
            message="Success ! Returned data",
            data=output_serializer.data
        ))

    def patch(self, request: Request, id: str):
        serializer = AlertInputUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = UpdateAlertsUseCase()
        alert_data = serializer.validated_data
        alert_data["id"] = id
        
        alert_updated = use_case.execute(alert_data, request.user.use_id)

        output_serializer = OutputSerializer(instance=alert_updated, many=True)

        return Response(format_response(
            success=True,
            message="Success ! The alert was updated",
            data=output_serializer.data
        ))

        
    def delete(self, request: Request):
        serializer = AlertsListInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = DeleteAlertsUseCase()
        alerts_deleted = use_case.execute(serializer.validated_data, request.user.use_id)

        if(not len(alerts_deleted) or (len(alerts_deleted) and alerts_deleted[0] <= 0)): return Response(format_response(
            success=True,
            message="Success ! You don't anyone register !",
            data={}
        ))

        return Response(format_response(
            success=True,
            data={},
            message="Success ! Data deleted."
        ))


class AlertsListView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        serializer = AlertsListInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = FindAllAlertsUseCase()
        alerts_founded = use_case.execute(serializer.validated_data, request.user.use_id)

        serializer_output = OutputSerializer(instance=alerts_founded, many=True)

        return Response(format_response(
            success=True,
            message="Success ! Data returned",
            data=serializer_output.data
        ))