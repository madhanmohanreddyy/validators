from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should not start with a')

def check_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('length is more than 5')

def check_for_age(value):
    if value<18 or value>45:
        raise forms.ValidationError('age is less than 18')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField(validators=[check_for_age])
    email=forms.EmailField(max_length=100)
    reenter_mail=forms.EmailField(max_length=100)
    botcatcher=forms.CharField(max_length=100,required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
       bot=self.cleaned_data.get('botcatcher')
       if len(bot)>=1:
        raise forms.ValidationError('botcatcher')




    def clean(self):
         e=self.cleaned_data.get('email')
         r=self.cleaned_data.get('reenter_mail')
         if e!=r:
             raise forms.ValidationError('emails are not matched')