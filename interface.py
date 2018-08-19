"""
===>    Programa: Interface
===>    Função: Criar GUI
===>    Descrição: Criar Widgets dinamicamente para uso da GUI
===>    Criador: Adenisio Pereira de Freitas
===>    Ano Criação: 2018
"""

#importando classe tkinter
from tkinter import *

class Interface(object):
    def __init__(self, instanciaTK):        #instanciando classe interface e passando como parametro um endereço da instacia de tkinter da classe principal
        self.tk = instanciaTK               #carregando variavel com parametro tkinter

#criando um lable para inserir as mensagens das caixas de aviso e entradas de dados
    def setLblText(self, txt):
        self.txt_lbl = Label(self.tk, text=txt)
        self.txt_lbl.pack()

#label mensagem para mosttrar resultado de funções processadas
    def setLblmensagem(self, txt):
        self.lbl_mensagem = Label(self.tk, text=txt)
        self.lbl_mensagem.pack()

#muda o valor da mensagem quando um processo é concluido
    def mudaMensagen(self, txt):
        self.lbl_mensagem['text'] = txt


#imput de entrada para dados, carrega dados do usuario, variaveis que receberam e manterão esses dados seram da classe DTO
    def setInput(self):
        self.txt_entry = Entry(self.tk)
        self.txt_entry.pack()
        return self.txt_entry               #temos que retornar toda a estrutura do entry

#cria um botão que recebe o texto e a função que usuari definir na classe principal
    def setBtn(self, txt, cmd):
        self.btn = Button(self.tk, text=txt, command=cmd)
        self.btn.pack()