from django import forms


class CurrencyForm(forms.Form):
    OPTIONS = (
        ("USD", "USD"),
        ("EUR", "EUR"),
        ("BTC", "BTC"),
        ("LTC", "LTC"),
        ("DOGE", "DOGE"),
        ("ETH", "ETH")
    )

    from_cur = forms.ChoiceField(required=True, choices=OPTIONS)
    to_cur = forms.ChoiceField(required=True, choices=OPTIONS)
