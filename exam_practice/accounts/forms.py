from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('first_name', 'last_name', 'email')