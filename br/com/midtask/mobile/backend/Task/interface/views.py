from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..infra.messages import format_response
from .serializer import (
    TaskInputSerializer,
    TaskOutputSerializer,
    TaskUpdateInputSerializer,
    TaskListInputSerializer
)
from ..application.use_cases.create_task_use_case import CreateTaskUseCase
from ..application.use_cases.find_unique_task_use_case import FindUniqueTaskUseCase
from ..application.use_cases.delete_task_use_case import DeleteTaskUseCase
from ..application.use_cases.update_task_use_case import UpdateTaskUseCase
from ..application.use_cases.findall_task_use_case import FindAllTaskUseCase

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

    def get(self, request: Request, id: str):
        try:    
            use_case = FindUniqueTaskUseCase()
            task_founded = use_case.execute(id, request.user.use_id)

            output_serializer = TaskOutputSerializer(instance=task_founded, many=True)

            return Response(format_response(
                success=True,
                message="Success ! Tasks founded.",
                data=output_serializer.data
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to get the task",
                err=e
            ))

    def delete(self, request: Request):
        try: 
            input_serializer =  TaskListInputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            use_case = DeleteTaskUseCase()
            tasks_deleted = use_case.execute(input_serializer.validated_data, request.user.use_id)
            if(not len(tasks_deleted) or (len(tasks_deleted) and tasks_deleted[0] <= 0)): return Response(format_response(
                success=True,
                message="Success ! You don't anyone register !",
                data={}
            ))

            return Response(format_response(
                success=True,
                data={},
                message="Success ! Data deleted."
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to delete the task",
                err=e
            ))
        
    def put(self, request: Request, id: str):
        try:
            input_serializer = TaskUpdateInputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            use_case = UpdateTaskUseCase()
            task_updated = use_case.execute(input_serializer.validated_data, id, request.user.use_id)

            return Response(format_response(
                success=True,
                message="Success ! Data updated.",
                data=task_updated
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to update task",
                err=e
            ))
        

class TaskListView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        try:
            input_serializer = TaskListInputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            use_case = FindAllTaskUseCase()
            tasks_founded = use_case.execute(input_serializer.validated_data, request.user.use_id)

            output_serializer = TaskOutputSerializer(instance=tasks_founded, many=True)
            return Response(format_response(
                success=True,
                message="Success ! Data returned.",
                data=output_serializer.data
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to findall tasks",
                err=e
            ))