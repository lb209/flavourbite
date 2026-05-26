from django import forms
from home.models import Profile


# ---------------- PROFILE FORM ----------------
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'city']