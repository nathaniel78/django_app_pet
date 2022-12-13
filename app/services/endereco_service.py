from ..models import EnderecoCliente

# Metodo para cadastrar endereço
def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)

# Método para listar endereco
def listar_endereco_id(id):
    return EnderecoCliente.objects.get(id=id)

# Método para editar cliente
def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.estado = endereco_novo.estado
    endereco_antigo.save(force_update=True)
    return endereco_antigo

# Método para remover endereço
def remover_endere(endereco):
    endereco.delete()