"""
===>    Programa: DAL (Data Access Layer)
===>    Função: Criar conecções e datasets para banco de dados baseado em programação de 3 camadas
===>    Descrição: Cria as funções e execução do banco de dados
===>    Criador: Adenisio Pereira de Freitas
===>    Ano Criação: 2018
"""
#sqite e nativo e pode se importado direto para o programa
import sqlite3

#criar função que abre conexão para banco de dados
class DAL(object):
    def __init__(self):                     #construtor padrão
        self.__tabela =  str()              #criando variavel que recebera vazio
        self.__connect = ''              #variavel para conexão do banco de dados
        self.__caminho = str()              #recebe caminho para o banco de dados, usaso somente se o caminho do banco de dados nãoestiver na mesmas pasta dos arquivos de negocios
        self.__str_sql = str()              #recebe os comandos SQL
        self.__mensagemSucesso = str()      #string que imprime mensagem de sucesso para usuario
        self.__error = str()                #string para gerar as mensagens de error de cenexão e execução do banco de dados

#setters e getters
    def setTabela(self, tabela):
        self.__tabela = tabela              #carregando nome da tabela, nome carregado em tempo de uso, definido no programa principal
    def getTabela(self):
        return self.nome                    #retornando nome da tabela para todas as classes que forem usar, o nome da tabela é carregado na chamada de instrução do programa principal
    def setCaminho(self, caminho):
        self.__caminho = caminho            #carregando caminho do banco de dados
    def getCaminho(self):
        return self.__caminho               #retornando caminho do banco de dados
    def setStrSql(self, str_sql):
        self.__str_sql = str_sql            #carregando string com comandos SQL
    def getStrSql(self):
        return self.__str_sql               #retorna string com valores de comandos SQL
    def setMensagem(self, mensagem):
        self.__mensagemSucesso = mensagem   #carregando string com mensagem de sucesso para usuario
    def getMensagem(self):
        return self.__mensagemSucesso       #retornando mensagem de sucesso
    def setMensagemError(self, msg_error):
        self.__error = msg_error            #carrega mensagem de error
    def getMensagemError(self):
        return self.__error                 #retiornando mensagem de error

 #abrindo conexão com banco de dados
    def openDatabase(self):
        try:
            self.__connect = sqlite3.connect('login.db')                              #abrindo connecção com banco de dados, se não existir será criado
            self.__mycursor = self.__connect.cursor()                                    #craindo um ponteiro para o banco de dados criado
            print(self.__connect)
            return self.__mycursor
        except:
            self.__error = "ERROR ao criar conecção com bando de dados\n Contacte seu Administrado"  #carrega mensagem de erro
            print(self.getMensagemError() )
            return self.getMensagemError()                                                           #retorna mensagem para ser visualizada pelo usuario

    #fchando connecçao com banco de dados, deve ser chamada logo apos uso do banco de dados
    def closeDatabase(self):
        if self.__connect:                                             #se a connecção estiver aberta
            self.__connect.close()                                      #feche

    #defininido função para executar comandos no banco de dados
    def executeComandos(self):
        try:
            self.__cursor = self.openDatabase()                         #abrindo conexão com banco de dados e atribindo ponteiro para uma variavel
            self.__cursor.execute(self.getStrSql())                     #com o ponteiro executamos o comando SQL
            self.closeDatabase()                                        #fechando a conexao com o banco de dados
            return self.getMensagem()                                   #retorna um aviso para usuario de comando executado com sucesso
        except:
            return self.getMensagemError()                              #se ouver erro retorna uma mensagem de aviso




d = DAL()
d.openDatabase()
d.closeDatabase()



