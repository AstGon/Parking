from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)

            # Verifica la contraseña del usuario
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # El usuario no existe
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
class EmailBackend:
    def authenticate(self, request, email=None, password=None, **kwargs):
        # Lógica de autenticación con correo electrónico y contraseña.
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        # Lógica para obtener el usuario por su ID.
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
