from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductProducerForm
# Create your views here.
def add_product(request):
    products = Products.objects.all()
    form  = ProductProducerForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return redirect('block_list')
    return render(request, 'add_product.html', {'form': form})
