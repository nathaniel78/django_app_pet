from ..models import Cliente

# Método para cadastrar cliente
def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco, cpf=cliente.cpf,
                           data_nascimento=cliente.data_nascimento, profissao=cliente.profissao)

# Método para listar clientes
def listar_cliente():
    return Cliente.objects.all()