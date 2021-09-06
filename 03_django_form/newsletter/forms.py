from django import forms


class MailForm(forms.Form):
    # 아래에 작성한 조건들이 Validation을 해준다
    # attr, widget 옵션은 HTML을 만들기 위해 존재
    name = forms.CharField(max_length=10, min_length=2, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(label='메일 내용', widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': '입력!',
            
        }
    ))
    check = forms.BooleanField(required=False)