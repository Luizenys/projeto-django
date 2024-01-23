from django import forms


class ShowForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    local = forms.CharField(max_length=200)
    endereco = forms.CharField(max_length=200)
    data = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))

    def clean_endereco(self):
        endereco = self.cleaned_data['endereco']
        txt = endereco.split(".")
        if (len(txt) < 2) or (txt[1] != "jpg" and txt[1] != "jpeg" and txt[1] != "png"):
            raise forms.ValidationError("Insira um formato válido de imagem!")
        return endereco

    def clean_data(self):
        data = self.cleaned_data['data']
        dia = data.day
        mês = data.month
        ano = data.year
        return data
