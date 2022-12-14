from ..models import pet_models


def cadastrar_pet(pet):
    pet_bd = pet_models.Pet.objects.create(
        nome=pet.nome,
        idade=pet.idade,
        categoria=pet.categoria,
        cor=pet.cor,
        peso=pet.peso,
        raca=pet.raca,
        genero=pet.genero,
        proprietario=pet.proprietario,
    )
    pet_bd.save()


# ------------buscar todos os pets de um determinado cliente
def listar_pets(id):
    pets = pet_models.Pet.objects.filter(proprietario=id).all()
    return pets


def listar_pets_all():
    return pet_models.Pet.objects.all()


def editar_pet(pet, pet_novo):
    pet.proprietario = pet_novo.proprietario
    pet.nome = pet_novo.nome
    pet.idade = pet_novo.idade
    pet.cor = pet_novo.cor
    pet.categoria = pet_novo.categoria
    pet.raca = pet_novo.raca
    pet.peso = pet_novo.peso
    pet.genero = pet_novo.genero
    pet.save(force_update=True)


def listar_pet_id(id):
    pet = pet_models.Pet.objects.get(id=id)
    return pet


def remover_pet(pet):
    pet.delete()
