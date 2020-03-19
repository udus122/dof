from django import forms


class DiagnosisForm(forms.Form):
    """
    FFS診断画面用のフォーム
    """
    A = forms.IntegerField(max_value=20, min_value=0, initial=0)
    B = forms.IntegerField(max_value=20, min_value=0, initial=0)
    C = forms.IntegerField(max_value=20, min_value=0, initial=0)
    D = forms.IntegerField(max_value=20, min_value=0, initial=0)
    E = forms.IntegerField(max_value=20, min_value=0, initial=0)
    factor = forms.CharField(max_length=5, required=False)
    answer = forms.IntegerField(max_value=2, min_value=0, required=False)

    def clean(self):
        cleaned_data = super().clean()
        factor = cleaned_data.get('factor')
        target = cleaned_data.get(factor)
        answer = cleaned_data.get('answer')
        result = target + answer
        print(f'answer: {answer}')
        print(f'result: {result}')
        self.data = self.data.copy()
        self.data[factor] = result
        return self.data
