from django import forms
from django.contrib.auth.models import User

from . models import Profile,Course



GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]
DEPARTMENT_CHOICES=[
        ('cs',"Computer sceince"),
        ('cm', "Commerce"),
        ('ms', "Medical sceince")
]


PURPOSE_CHOICES = [
        ('enquiry', "Enquiry"),
        ('purchase', "Purchase"),
        ('return', "Return")
]
class ProfileCreationForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={'class':'inline-flex'}))
    department=forms.ChoiceField(choices=DEPARTMENT_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    purpose=forms.ChoiceField(choices=PURPOSE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    #user = forms.HiddenInputField()
    class Meta:
        model = Profile
        #exclude = ('user',)
        fields = ['name','dob','age','gender','phone','mailid','address','department','purpose','user']
        labels={'name':'Full Name',
                'dob':'Date of birth',
                'age':'Age',
                'gender':'Gender',
                'phone':'Mobile No',
                'mailid':"Mail ID",
                'address':'Address',
                'department':"Department",

                'purpose':"Purpose"}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'mailid':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),

        }

        #def __init__(self, *args, **kwargs):
        #    user = kwargs.pop('user', '')
         #   super(ProfileCreationForm, self).__init__(*args, **kwargs)
         #   self.fields['username'] = forms.ModelChoiceField(
         #       queryset=User.objects.filter(username=user))
    #def __init__(self,*args,**kwargs):
     #   super().__init__(*args,**kwargs)
     #   self.fields['course'].queryset=Course.objects.none()

      #  if 'department' in self.data:
      #      try:
       #         department_id=int(self.data.get('department'))
       #         self.
