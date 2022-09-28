from django import froms
from .models import Core

class PostForm(forms.modelForm):
    class Meta:
        model   =   Core
        fields  =   "__all__"