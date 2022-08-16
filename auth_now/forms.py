from django import forms
from auth_now.models import UserBioInfo



class UserBioForm(forms.ModelForm):
    class Meta:
        model = UserBioInfo
        fields = "__all__"
        exclude = ("user_fk", )


