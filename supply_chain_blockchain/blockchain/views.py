from django.shortcuts import render, redirect, get_object_or_404
from .models import Block
from .forms import  BlockForm, TransactionForm
from django.contrib.auth.decorators import login_required, permission_required
from hashlib import sha256
# Create your views here.

def calculate_hash(content):
    first_hash = sha256(content.encode()).hexdigest()
    second_hash = sha256(first_hash.encode()).hexdigest()
    return second_hash


def proof_of_work(block_hash, current_transactions):
    difficulty = 2
    computed_hash = block_hash
    computed_hash = calculate_hash(current_transactions)
    return computed_hash


@login_required
def block_list(request):
    blocks = Block.objects.all()
    return render(request, 'block_list.html', {'blocks': blocks})


@login_required
@permission_required('blockchain.add_block', login_url="/login")
def block_create(request):
    blocks = Block.objects.all()
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        registro_animal = request.POST['registro_animal']
        volume = request.POST['volume']
        dia_horario = request.POST['dia_horario']

        tempo_armazenamento = request.POST['tempo_armazenamento']
        temperatura_armazenamento = request.POST['temperatura_armazenamento']
        ph = request.POST['ph']


        registro_veiculo1 = request.POST['registro_veiculo1']
        temperatura_transporte = request.POST['temperatura_transporte']
        tempo_transporte = request.POST['tempo_transporte']

        volume_resfriamento = request.POST['volume_resfriamento']
        dia_hora_resfriamento = request.POST['dia_hora_resfriamento']
        temperatura_resfriamento = request.POST['temperatura_resfriamento']
        ph_resfriamento = request.POST['ph_resfriamento']


        volume_envase = request.POST['volume_envase']
        dia_hora_envase = request.POST['dia_hora_envase']
        lote = request.POST['lote']

        registro_veiculo_final = request.POST['registro_veiculo_final']
        temperatura_transporte_final = request.POST['temperatura_transporte_final']
        tempo_transporte_final = request.POST['tempo_transporte_final']

        current_transactions = (str(registro_animal) + "\n" + str(volume) + "\n" + str(dia_horario) + "\n" + 
                               str(tempo_armazenamento) + "\n" + str(temperatura_armazenamento) + "\n" + str(ph) + "\n" + 
                               str(registro_veiculo1) + "\n" + str(temperatura_transporte) + "\n" + str(tempo_transporte) + "\n" + 
                               str(volume_resfriamento) + "\n" + str(dia_hora_resfriamento) + "\n" + str(temperatura_resfriamento) + "\n" + str(ph_resfriamento) + "\n" +
                               str(volume_envase) + "\n" + str(dia_hora_envase) + "\n" + str(lote) + "\n" + 
                               str(registro_veiculo_final) + "\n" + str(temperatura_transporte_final) + "\n" + str(tempo_transporte_final))
        
        block_hash = proof_of_work(calculate_hash(current_transactions), current_transactions)
        instance = Block(index=len(blocks), previous_hash=blocks[len(blocks) - 1],current_transactions=current_transactions,nonce=0,hash=block_hash)
        instance.save()
        return redirect('block_list')
    return render(request, 'block_form.html', {'form': form})

@login_required
def block_view(request, hashcode):
    block = get_object_or_404(Block, pk=hashcode)
    form = BlockForm(instance=block)

    if(form.is_valid()):
        return redirect('block_list')
    return render(request, 'block_form.html', {'form':form})