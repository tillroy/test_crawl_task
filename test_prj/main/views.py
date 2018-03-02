from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

from .forms import CurrencyForm
from .models import CurrencyСorrelation, CurrencyValue

# Create your views here.


def main(request):
    title = "Main Page"

    currs = CurrencyСorrelation.objects.all()

    form = CurrencyForm(request.POST or None)
    # confirm_message = None

    if form.is_valid():
        # print(request.POST)

        from_cur = form.cleaned_data["from_cur"]
        to_cur = form.cleaned_data["to_cur"]

        _curr_record = CurrencyСorrelation(from_cur=from_cur, to_cur=to_cur)
        _curr_record.save()

        # confirm_message = "Currency successfully added: {}->{}".format(from_cur, to_cur)
        return redirect("main")

    context = {"title": title, "form": form, "currs": currs}
    # context = {"confirm_message": confirm_message, "title": title, "form": form, "currs": currs}

    return render(request, 'main/main.html', context)


def curr_list(request, pk):
    title = "Currency List Page"

    values = CurrencyValue.objects.filter(correlation=pk)

    context = {"title": title, "values": values}
    return render(request, 'main/list.html', context)

    # currs = CurrencyСorrelation.objects.all()