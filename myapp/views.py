
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import FAQ
from .forms import FAQForm

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})

def faq_detail(request, pk):
    # faq = FAQ.objects.get(pk=pk)
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'faq_detail.html', {'faq': faq})

def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faq_create.html', {'form': form})

def faq_update(request, pk):
    faq = FAQ.objects.get(pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faq_update.html', {'form': form})

def faq_delete(request, pk):
    faq = FAQ.objects.get(pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    return render(request, 'faq_delete.html', {'faq': faq})


