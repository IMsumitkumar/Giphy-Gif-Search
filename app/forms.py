from django import forms

class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100,
                    widget= forms.TextInput(attrs={'class':'form-control search-form-control  ml-lg-auto',
				   'placeholder':'Search content...'}), label='')

    page_lim_field = forms.IntegerField(
                    widget= forms.TextInput(attrs={'class':'form-control search-form-control  ml-lg-auto',
				   'placeholder':'Limit : Please enter an integer ...'}), label='')

    