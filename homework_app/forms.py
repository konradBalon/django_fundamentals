from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)


class MovieForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    year = forms.CharField(label='year', max_length=100)
    director = forms.CharField(label='director', max_length=100)
    rating = forms.FloatField(label='rating')
    screenplay = forms.CharField(label='screenplay', max_length=100)
