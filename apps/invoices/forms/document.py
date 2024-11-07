from django import forms

class DocumentForm(forms.Form):
    """Document form for file upload."""

    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control w-50",
            },
        ),
        label="Загрузите файл накладной в формате PDF или её изображение",
        required=False,
    )