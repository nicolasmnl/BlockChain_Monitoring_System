from django.shortcuts import render, redirect, get_object_or_404
from .models import Block
from .forms import BlockForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def block_list(request):
    blocks = Block.objects.all()
    return render(request, 'block_list.html', {'blocks': blocks})


def block_create(request):
    blocks = Block.objects.all()
    form = BlockForm(request.POST or None)

    if form.is_valid():
        block = form.save(commit=False)
        block.index = len(blocks)
        new_hash = proof_of_work(block, block.current_transactions)
        block.hash = new_hash
        form.save()
        return redirect('block_list')
    return render(request, 'block_form.html', {'form': form})

def proof_of_work(block, current_transactions):
    difficulty = 1
    block.nonce = 0
    computed_hash = block.hash
    while not (computed_hash.endswith('0' * difficulty) and ('55' * difficulty) in computed_hash):
        block.nonce += 1
        computed_hash = block.calculate_hash(current_transactions)
        return computed_hash