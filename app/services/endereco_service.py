from ..models import EnderecoCliente

# Metodo para cadastrar endereço
def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, cidade=endereco.estado, estado=endereco.estado)