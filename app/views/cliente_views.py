from django.shortcuts import render
from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoClienteForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service

# Método listar
def listar_clientes(request):
    clientes = cliente_service.listar_cliente()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# Método cadastro
def cadastrar_cliente(request):
    # validando metodo POST
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)

        # validando form cliente
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            email = form_cliente.cleaned_data['email']
            cpf = form_cliente.cleaned_data['cpf']
            data_nascimento = form_cliente.cleaned_data['data_nascimento']
            profissao = form_cliente.cleaned_data['profissao']

            # validando form endereço
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data['rua']
                cidade = form_endereco.cleaned_data['cidade']
                estado = form_endereco.cleaned_data['estado']

                # armazenando na entidade endereco os valores do form endereco
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)

                # Salvando endereço
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)

                # armazenando na entidade cliente os valores do form cliente
                cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento,
                                           profissao=profissao, endereco=endereco_bd)

                # Salvando cliente
                cliente_service.cadastrar_cliente(cliente_novo)

    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()

    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})