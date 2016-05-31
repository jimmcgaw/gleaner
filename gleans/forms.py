from django import forms
from .models import Crop

class CropForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ basically make all fieldnames bootstrappy """
        super(CropForm, self).__init__(*args, **kwargs)
        for field_name, value in self.fields.iteritems():
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Crop
        fields = ['first_name', 'last_name', 'phone_number', 'contact_address1',
            'contact_address2', 'contact_city', 'contact_state', 'contact_zip',
            'crop_address1', 'crop_address2', 'crop_city', 'crop_state', 'crop_zip',
            'crop_type', 'receipt_preference', 'crop_description']
