"""
===>    Programa: DLL (Data Logic Layer)
===>    Função: Criar logica de acesso para camadas dos objetos
===>    Descrição: Criar Widgets dinamicamente para uso da GUI
===>    Criador: Adenisio Pereira de Freitas
===>    Ano Criação: 2018
"""
# importando o sqlite e DAL(Data Access Layer
from sqlite3 import *
from DAL import *

dal = DAL()

"""
===> Criando  classe DLL para a logica de conecção, procedures e datasets
"""


class DLL(object):
    def __init__(self):
        self.__tabela = str()                   #cria uma string para nome de tabela
        self.__stringSQL = str()                #string para receber instruções SQL
        self.__strSucesso  = str()              #Mensagem de sucesso para carregar aviso para usuario
        self.__error = str()                    #string para mensagens de ERROR par usuario

    def dalComandos(self):
        dal.setMensagem(self.__stringSQL)                            # Carregando mensagem de sucesso
        dal.setMensagemError(self.__error)                           # Carregando mensagem de ERROR
        self.__strSucesso = dal.executeComandos()                    #executa comandos dentro da classe DLL

    def setTabela(self):
        self.__tabela = dal.getTabela()          # tabela recebe nome que sera carregado na classe DAL no metodo setTabela

    # Criando uma função que cria a tabela se ela não existir
    def criar_Tabela(self):
        try:
            self.__stringSQL = ("CREATE TABLE IF NOT EXISTS {0}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT," \
                               "nome VARCHAR(50)," \
                               "senha VARCHAR(8))".format(self.__tabela))        #Cria uma string para crair uma tabela login
            self.__strSucesso = 'Tabela LOGIN criada com Sucesso'                #Criando mensagem Bem Sucedido
            self.__error = 'ERROR\nTabela não encontrada'                        #Craindo mensagem de error
            dal.setCaminho('')                                                   #Carregando string com o caminho logico do sistema para db
            self.dalComandos()                                                   #executa comandos dentro da classe DLL
            return self.__strSucesso                                            #retorna mensagem para classe principal
        except:
            # se não for criada retornamos uma mensagem de erro
            self.__error = 'ERROR ao criar tabela Login\nContacte o Administrador'
            return self.__error



