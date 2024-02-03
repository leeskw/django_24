from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Enter email address"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Confirm password"}))
    class Meta:
        model = get_user_model() 
        fields = ["email", "username", "password1", "password2"]
        
  
class UpdateProfileForm(UserChangeForm):  
    password = None
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'bio', 'phone', 'role', 'profile_pic', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'          
            self.fields[field_name].widget.attrs['placeholder'] = 'Enter ' + field_name.replace('_', ' ')  # OK!
            if field_name == 'profile_pic':
                self.fields[field_name].widget.attrs['placeholder'] =  'Upload image' 
        
        
# class UpdateProfileForm(forms.ModelForm):

    # class Meta:
    #     models = get_user_model()
    #     # fields = ('first_name', 'last_name', 'username', 'email', 'address', 'bio', 'phone', 'role', 'profile_pic', ) 
                
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # for field_name in self.fields:
        #     self.fields[field_name].widget.attrs['class'] = 'form-control'            
    
        # self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        # self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        # self.fields['address'].widget.attrs['placeholder'] = 'Enter address'
        # self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        # self.fields['profile_pic'].widget.attrs['placeholder'] = 'Upload image'
        # self.fields['bio'].widget.attrs['placeholder'] = 'Enter bio'
        # self.fields['phone'].widget.attrs['placeholder'] = 'Enter phone'
        # self.fields['role'].widget.attrs['placeholder'] = 'Enter role'

       
        
# class UpdateProfileForm(forms.ModelForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter firstname"}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter lastname"}))
#     username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter username"}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Enter email address"}))
#     profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Upload image"}))
#     address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter address"}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter phone"}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Enter bio"}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter phone"}))
#     role = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter role"}))

#     class Meta:
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'username', 'email', 'address', 'bio', 'phone', 'role', 'profile_pic', )
