from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate
from django.db.models import Q


user = get_user_model()

USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*$'

class UserLoginForm(forms.Form):
    query = forms.CharField(max_length=120,label="username/email")
    password = forms.CharField(max_length=20, label="Pasword")
    
    def clean(self,*args,**kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        # the_user = authenticate(username=username,password=password)
        # if not the_user:
        #     raise forms.ValidationError("Invalid Credential")
        """
        when you are using password_check them make sure first() in filter method
        """
        user_obj_final = user.objects.filter(
                                         Q(username=query) |
                                         Q(email=query)   
                                      ).distinct()
        if not user_obj_final.exists() and user_obj_final.count() != 1:
            raise forms.ValidationError("Invalid Creedential")
        else:
            user_obj = user_obj_final.first()
            if not user_obj.check_password(password):
                raise forms.ValidationError("Invalid Credential")
            if not user_obj.is_active:
                raise forms.ValidationError("Inactive user")
        self.cleaned_data['user_obj'] = user_obj
        return super(UserLoginForm,self).clean(*args,**kwargs)
        
    
    # def clean_username(self,*args,**kwargs):
    #     username = self.cleaned_data.get('username')
    #     user_qs = user.objects.filter(username=username)
    #     user_exist = user_qs.exists()
    #     if not user_exist and user_qs.count() != 1:
    #         raise forms.ValidationError("Invalid Credential")
    #     return username 
   

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = user
        fields = ('email', 'password', 'username', 'is_active', 'is_admin','is_staff')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
