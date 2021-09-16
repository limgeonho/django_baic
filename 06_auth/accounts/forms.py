from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        # username은 변경 불가능 하게!
        fields = ('first_name', 'last_name', 'email')