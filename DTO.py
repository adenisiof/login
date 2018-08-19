"""
===>     Programa: DTO (Data Transfer Obejct)
===>     Função: Crair objetos especificos para separar cada tipo de classe de objetos
===>     Descrição: Esse programa em especifico ira criar controle para armazenar todos os dados do usuario como nome senha e email
===>     Criador: Adenisio Pereira de Freitas
===>     Ano Criação: 2018
"""
class dto(object):
#construindo as variaveis na hora que a classe e intanciada
    def __init__(self):
        self._nome = str()          #criando uma variavel para nome de usario e tribuindo valor vazio
        self._senha = int()         #craindo a variavel para senha do usario e atribuindo valor 0

#setters e getters para as vriaveis do construtor (nome e senha)
    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome.get()

    def setSenha(self, senha):
        self._senha = senha

    def getSEnha(self):
        return self._senha

