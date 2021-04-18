from django.shortcuts import render, redirect, get_object_or_404
from .models import Block
from .forms import BlockForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def block_list(request):
    blocks = Block.objects.all()
    return render(request, 'block_list.html', {'blocks': blocks})


def block_create(request):
    form = BlockForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('block_list')
    return render(request, 'block_form.html', {'form': form})