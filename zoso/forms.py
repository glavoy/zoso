from django import forms
from .models import Post, Comment, Profile
from django.db.models import Q

# This form is used to add a new post
# Contains a Textarea input and an Image uplolad
# It also 'hides' the label for the text input
class PostForm(forms.ModelForm):
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': 'Post something here...'
        }))

    image = forms.ImageField(required=False, label="")

    class Meta:
        model = Post
        fields = ['text', 'image']



# This form is used to add a comment to a previous post
# Contains a Textarea input
# It also 'hides' the label for the text input
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Add comment...'}
        ))

    class Meta:
        model = Comment
        fields = ['comment']



# This form is used to display radio buttons for each contact
# The user can then select which user they want to caht with
class ChatForm(forms.ModelForm):

    # Overriding the __init__ method so we can get the current user
    # so that we can display only contacts of the current user
    # rather than anyone who is a contact of any user
    def __init__(self, *args, **kwargs):
        # Grants access to the request object so that 
        # only contacts of the current user are displayed

        self.request = kwargs.pop('user')
        super(ChatForm, self).__init__(*args, **kwargs)
        # A rather complex query that gets the only the contacts of the current user
        self.fields['contacts'].queryset = Profile.objects.values_list('contacts__username', flat=True).distinct().exclude(contacts__username=None).filter(~Q(contacts__username=self.request.username)).order_by('contacts__username')
        self.fields['contacts'].label = ""

    class Meta:
        model = Profile
        fields = ['contacts']

    # We don't need to specify the queryset since it is defined above
    contacts = forms.ModelChoiceField(
        queryset = None,
        widget=forms.RadioSelect
    )



