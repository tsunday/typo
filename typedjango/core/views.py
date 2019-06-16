from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Driver
from core.serializers import DriverSerializer


class DriverView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request: HttpRequest) -> Response:
        drivers = Driver.objects.all()
        return Response(DriverSerializer(drivers, many=True).data)
