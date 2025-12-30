from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..infra.messages import format_response
from .serializer import (
    AlertInputSerializer,
    OutputSerializer
)
from ..application.use_cases.create_alerts_use_case import CreateAlertsUseCase

# Create your views here.
class AlertsView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        try:
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
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to insert the alert",
                err=e
            ))