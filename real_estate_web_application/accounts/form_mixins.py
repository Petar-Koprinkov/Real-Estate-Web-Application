from django import forms


class DisabledMixin(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field in self.disabled_fields or self.disabled_fields == '__all__':
                self.fields[field].disabled = True
