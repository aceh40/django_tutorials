import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

##############################
### - test stuff:
##############################
#
# from .models import NoSugar
#
#
# class NoSugarForm(forms.ModelForm):
#     """ Simple Form to track No Sugar habit.
#         Do something quick and dirty.
#     """
#     class Meta:
#         model = NoSugar
#         fields = ('entry_date', 'completed', 'note',)



