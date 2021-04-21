from django.shortcuts import render, redirect, get_object_or_404
from .models import Block
from .forms import BlockForm
from django.contrib.auth.decorators import login_required
from hashlib import sha256
# Create your views here.

def calculate_hash(content):
    first_hash = sha256(content.encode()).hexdigest()
    second_hash = sha256(first_hash.encode()).hexdigest()
    return second_hash


def proof_of_work(block_hash, current_transactions):
    difficulty = 2
    nonce = 0
    computed_hash = block_hash
    nonce += 1
    computed_hash = calculate_hash(current_transactions)
    return (computed_hash, nonce)




def block_list(request):
    blocks = Block.objects.all()
    return render(request, 'block_list.html', {'blocks': blocks})


def block_create(request):
    blocks = Block.objects.all()
    form = BlockForm(request.POST or None)

    if form.is_valid():
        block = form.save(commit=False)
        block.index = len(blocks)
        values = proof_of_work(block.hash, block.current_transactions)
        block.previous_hash = blocks[len(blocks) - 1]
        block.hash = values[0]
        block.nonce = values[1]
        form.save()
        return redirect('block_list')
    return render(request, 'block_form.html', {'form': form})




