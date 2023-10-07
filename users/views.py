from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsNewUser
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated | IsNewUser]


# def user_logout(request):
#     logout(request)
#     return Response(status=200)

class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=200)

# def create_user(request):
#     user = User.objects.create_user(
#
#     )
#     return
