"""
===>   Programa: login
===>   Função: Autentica usuario e senha em banco de dados
===>   Descrição: Programa principal, insere os Widgets na interface, armazena os dados recebidos na classe DTO e chamas as função de manipulaão do banco de dados da classe DAL
===>   Criador: Adenisio Pereira de Freitas
===>   Ano Criação: 2018
"""

#importantdo classes
from tkinter import *
from interface import Interface
from DAL import *
from DTO import *
from DLL import *


tk = Tk()                                   #instanciando classe tkinter e inserindo tamanho a janela
tk.geometry('400x300')
dal = DAL()                                 #instanciando a classe responsavel por criar as prosedures e datasets
dto = dto()                                 #instanciando a classe que armazena os dados do usuario para tratar
dll = DLL()                                 #instanciando a classe que cria a logica SQL

mensagem = dll.criar_Tabela()               #criando a tabela quando carrega o programa, a tabela retorna um aviso, temos que mostrar esse aviso para o usuario na lable criada abaixo do botão inserir novo
interface = Interface(tk)                   #intanciando classe Interface responsavel por criar os Widgets na tela principal

#criando o campos para entrada de dados
interface.setLblText('Nome')                #criando label para identificar entrada nome de usuario
dto.setNome(interface.setInput())           #craindo um textbox para usuario inserir nome, e automaticamente ja passamos o nome para classe DTO salvar a entrada na memoria
interface.setLblText('Senha')               #criando label para identificar entrada de senha do usuario
dto.senha = interface.setInput()

""""
====> botão para inserir os dados
====> Quando clicarmos no botão os dados da caixa de nome e senha devem ser inserido na tabela login,
====> usamos a função lambda para permitir a chmada de função das classes externa (classe: Interface / classe: dto)
"""
interface.setBtn('Inserir', lambda:interface.mudaMensagen(dto.getNome()))

interface.setLblmensagem("mensagem na tela")      #criando label para mensagens usuario sobre sucesso e erro no sistema


print(mensagem)







tk.mainloop()
