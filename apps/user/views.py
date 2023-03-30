from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import views

from apps.user import models, serializers
from apps.user.models import User
from apps.user.permissions import IsAdminUser, IsAdminUserOrMerchantReadOnly
from apps.user.serializers import UserSerializer, ClientModelSerializer, MerchantModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class LoginView(views.TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = [AllowAny,]


class ChangePasswordView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated,]


class UpdateProfileView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UpdateUserSerializer
    permission_classes = [IsAuthenticated,]


class ClientModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.CLIENT)
    serializer_class = ClientModelSerializer
    permission_classes = [IsAdminUserOrMerchantReadOnly, IsAuthenticated]


class MerchantModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.MERCHANT)
    serializer_class = MerchantModelSerializer
    permission_classes = [IsAdminUserOrMerchantReadOnly, IsAuthenticated]
