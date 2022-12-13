from ..models import Cliente

# Método para cadastrar cliente
def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco, cpf=cliente.cpf,
                           data_nascimento=cliente.data_nascimento, profissao=cliente.profissao)

# Método para listar clientes
def listar_cliente():
    return Cliente.objects.all()

# Método para listar cliente por id
def listar_cliente_id(id):
    return Cliente.objects.get(id=id)

# Método para editar cliente
def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.email = cliente_novo.email
    cliente.endereco = cliente_novo.endereco
    cliente.cpf = cliente_novo.cpf
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.profissao = cliente_novo.profissao
    cliente.save(force_update=True)

# Método para remover cliente
def remover_cliente(cliente):
    cliente.delete()