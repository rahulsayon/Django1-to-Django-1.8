from django import forms
from . models import Blog
from django.utils.text import slugify

SOME_CHOICES = [
    ('db-value' , 'DB Value1'),
    ('db-value2' ,'DB Value2'),
    ('db-value3' , 'DB Value3')
]
INT_CHOICES = [ tuple([x,x]) for x in range(0,120)  ]

class SearchForm(forms.Form):
    some_text = forms.CharField(widget=forms.Textarea(attrs={ "rows" : 4 , "cols" : 40 }))
    boolean = forms.BooleanField()
    choices = forms.CharField(label="Text" , widget=forms.Select(choices=SOME_CHOICES))
    integer = forms.IntegerField(initial=101 , widget=forms.Select(choices=INT_CHOICES))
    email = forms.EmailField()
    
    def __init__(self,*args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)
        self.fields["some_text"].initial = "some text fields 1"
    
    def clean_integer(self,*args,**kwargs):
        integer = self.cleaned_data.get('integer')
        if integer < 10:
            raise forms.ValidationError("The interger must be greater then 10 ")
        return integer
    
    



class SearchModelForm(forms.ModelForm):
    # title = forms.CharField(max_length=120,
    #                         label = "Some This",
    #                         help_text="Please fill",
    #                         error_messages={
    #                             "required" : "The title fields is required"
    #                          })
    class Meta:
        model = Blog
        fields = [
            'user',
            'title',
            'slug'
        ]
        """
            The way custome message of putting message in form
        """
        # labels = {
        #     "title" : "this is title label",
        #     "slug" : "This is slug"
        # }
        # help_text = {
        #     "title" : "This is title label",
        #     "slug" : "This is slug"
        # }
        # error_message = {
        #      "title" : { 
        #             "max_length" : "The title too long",
        #             "riquired" : "This is required"
        #          }
        # }
        """
            The 2nd custome message way of putting message in form
        """
    def __init__(self,*args,**kwargs):
        super(SearchModelForm,self).__init__(*args,**kwargs)
        self.fields["title"].widget = forms.Textarea()
        self.fields["title"].error_message = {
          "max_length" : "The title too long",
           "riquired" : "This is required"  
        }
        """
            The 3 custome message way of putting message in form
        """
        
        for field in self.fields.values():
            field.error_message = {
                "required" : "You are know , {fieldname} is required".format(fieldname=field.label)
            }
    
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        return title


    """
        PreSave Method while Saving
    """
    # def save(self,commit=True,*args,**kwargs):
    #     obj = super(SearchModelForm,self).save(commit=False,*args,**kwargs)
        
        
    #     # obj.title = "New rAHUL"
    #     obj.slug = slugify(obj.title)
    #     if commit:
    #         obj.save()
    #     return obj