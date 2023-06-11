from django.forms import ModelForm
from .models import MakeAnAppointment


class MakeAnAppointmentForm(ModelForm):
    class Meta:
        model = MakeAnAppointment
        fields = ['name', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'makeanapp_input'})