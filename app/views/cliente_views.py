from django.shortcuts import render, redirect
from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoClienteForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service

# Método listar
def listar_clientes(request):
    clientes = cliente_service.listar_cliente()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

# Método listar cliente por id
def listar_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/listar_cliente.html', {'cliente': cliente})

# Método remover cliente
def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    endereco = endereco_service.listar_endereco_id(cliente.endereco.id)

    if request.method == 'POST':
        cliente_service.remover_cliente(cliente)
        endereco_service.remover_endereco(endereco)

        return redirect('listar_clientes')

    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})

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

                # Redirecionando
                return redirect('listar_clientes')

    # Se não, voltar o formulário em branco
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()

    # Carregar página do form
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})

# Método de edição
def editar_cliente(request, id):
    # Recebendo instancia
    cliente_editar = cliente_service.listar_cliente_id(id)
    cliente_editar.data_nascimento = cliente_editar.data_nascimento.strftime('%Y-%m-%d')
    form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)
    endereco_editar = endereco_service.listar_endereco_id(cliente_editar.endereco.id)
    form_endereco = EnderecoClienteForm(request.POST or None, instance=endereco_editar)

    # Validando form cliente
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data["nome"]
        email = form_cliente.cleaned_data["email"]
        cpf = form_cliente.cleaned_data["cpf"]
        data_nascimento = form_cliente.cleaned_data["data_nascimento"]
        profissao = form_cliente.cleaned_data["profissao"]

        # Validando form endereço
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]

            # Armazenando valores form endereço
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)

            # Editando endereço e armazenando em nova variavel
            endereco_editado = endereco_service.editar_endereco(endereco_editar, endereco_novo)

            # Armazenando valores do form e instanciando objeto
            cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_editado)

            # Editando cliente
            cliente_service.editar_cliente(cliente_editar, cliente_novo)

            # Redicionar
            return redirect('listar_clientes')

    # Carregar página do form
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente ,'form_endereco': form_endereco})