from rest_framework.decorators import api_view
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .serializer import UserSerializer

User = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(email=username) | Q(username=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None

class EmailOrUsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get('email') or request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return None

        user = EmailOrUsernameModelBackend().authenticate(request, username=username, password=password)
        if user:
            return (user, None)
        raise AuthenticationFailed('Invalid email/username or password.')

@api_view(['POST'])
def login(request):
    user = authenticate(request=request)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response("Invalid email or password.", status=status.HTTP_400_BAD_REQUEST)
