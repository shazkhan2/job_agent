from rest_framework import generics, permissions, status
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token # REMOVE THIS - not used with Simple JWT for registration
from django.contrib.auth import get_user_model # Use get_user_model for consistency

User = get_user_model() # Define User at module level
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user_id': user.pk,
            'email': user.email,
            'message': 'User registered successfully. Now log in to get tokens.'
        }, status=status.HTTP_201_CREATED)
