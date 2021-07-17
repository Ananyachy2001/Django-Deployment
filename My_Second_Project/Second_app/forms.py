from django import forms
#from Second_app.models import Album,Musician
from Second_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"
        #exclude =['first_name','last_name']
        #fields = ('first_name','last_name')


class AlbumForm(forms.ModelForm):
    release_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"





























#def even_or_not(value):
#    if value%2 ==1:
#        raise forms.ValidationError("Please Insert an even number!")

#class user_form(forms.Form):
    #name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    #number_field = forms.IntegerField(validators=[validators.MaxValueValidator(15),validators.MinValueValidator(5)])
    #number_field = forms.IntegerField(validators=[even_or_not])
#    user_email = forms.EmailField()
#    user_vmail = forms.EmailField()

#    def clean(self):
#        all_cleaned_data = super().clean()
#        user_email = all_cleaned_data['user_email']
#        user_vmail = all_cleaned_data['user_vmail']

#        if user_email != user_vmail:
#            raise forms.ValidationError("Fields Don't match")




    #boolean_field = forms.BooleanField(required=False)
    #field = forms.CharField(max_length=15,min_length=5)
    #CHOICES = (('1','First'),('2','Second'),('3','Third'),('4','Fourth'))
    #choices=(('','--SELECT OPTION--'),('1','First'),('2','Second'),('3','Third'),('4','Fourth'))
    #field=forms.ChoiceField(choices=choices,required=False)
    #choices = (('A','A'),('B','B'),('C','C'))
    #field=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    #choices=(('','--SELECT OPTION--'),('1','First'),('2','Second'),('3','Third'),('4','Fourth'))
    #field=forms.MultipleChoiceField(choices=choices,required=False)
    #choices = (('A','A'),('B','B'),('C','C'))
    #field=forms.MultipleChoiceField(choices=choices,widget=forms.CheckboxSelectMultiple)





    #<label for="user_name">Full Name</label>
    #<input type="text" name="user_name" value="" placeholder="Enter your full name" required>
    #user_name = forms.CharField(required=True, label = "Full Name", widget=forms.TextInput(attrs={'placeholder': 'Enter your full name', 'style' : 'width:300px'}))

    #user_dob = forms.DateField(label="Date Of Birth",widget=forms.TextInput(attrs={'type': 'date' }))


    #<label for="email_name">Email</label>
    #<input type="email" name="email_name" value="" required>
    #email_name = forms.EmailField(required=True, label = "User Email",widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
