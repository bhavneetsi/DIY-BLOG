from django import forms

class CreateComment(forms.Form):

    comment=forms.CharField(widget=forms.Textarea)
    user=forms.CharField(max_length=50)


"""
    def clean_comment(self):
        data = self.cleaned_data['comment']
        return data
"""        