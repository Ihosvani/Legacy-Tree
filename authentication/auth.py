from django.contrib.auth.backends import BaseBackend
from user.models import User
class auth(BaseBackend):
    def authenticate(self, request, username=None, password=None, email=None):
        print('using custom backend')
        try:
            #check for username in the DB
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                #check for email in the DB
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return None
        #compare both password, if they dont match it will send None
        
        if not user.password == password:
            return None

        return user
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
