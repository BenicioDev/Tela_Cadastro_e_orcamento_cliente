# Tela_Cadastro_e_orcamento_cliente
# Tela que fornece informações para fazer o orçamento do cliente juntamente com seu cadastro
from html import entities
from importlib.metadata import entry_points
from msilib.schema import ComboBox
import numbers
from operator import contains 
import tkinter as tk 
from tkinter import CENTER, W, Entry, Grid, ttk
import datetime as dt
import tkinter as tk
from xml.dom import ValidationErr

lista_materiais = ["Fios","Caixa de metal","parafusos","Placa 1", "Placa 2", "Circuito Placa"]
lista_serviços = ["Reprogramação de automação", "Restauração sistema", "Remontagem de manutenção", "Remonstagem por defeito", "Reparo preventivo"]

janela = tk.Tk()

#título da janela
janela.title("Engreno's - CADASTRO E SELEÇÃO DE SERVIÇOS")
janela.maxsize #(C:\Users\Gabriel\Pictures\code-syntax-dark-minimal-4k-mr-1366x768.jpg)

#--------------------------------------------------------------------------------------
#####Labels de cadastro - NOME;
nome = tk.Label(text="Digite o nome do Cliente: ")
nome.grid(row=1, column=0, padx=10, pady= 10, sticky='nswe', columnspan = 1) ###'grid' põe dentro da janela
################# linha de escrever - NOME;
Entry_nome = tk.Entry()
Entry_nome.grid(row=1, column=1, padx=10, pady= 10, sticky='nswe', columnspan = 1)
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
#####Labels de cadastro - CONTATO;
contato = tk.Label(text="Digite o número de contato: ")
contato.grid(row=3, column=0, padx=10, pady= 10, sticky='nswe', columnspan = 1)

##################################### linha de escrever - CONTATO;
Entry_contato = tk.Entry()
Entry_contato.grid(row=3, column=1, padx=10, pady= 7, sticky='nswe', columnspan = 1)
################################################Linha escrever - Email
email = tk.Label(text="Digite seu email de contato: ")
email.grid(row=5, column=0, padx=10, pady= 10, sticky='nswe', columnspan = 1)
Entry_email = tk.Entry()
Entry_email.grid(row=5, column=1, padx=10, pady= 10, sticky='nswe', columnspan = 1)
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#####Labels descrição serviço
descrição_peça = tk.Label(text='Seleção de Peças fornecidas: ')
descrição_peça.grid(row=7, column=0)
################### Caixa seleção PEÇAS
combobox_selecionar_peças = ttk.Combobox(values=lista_materiais)
combobox_selecionar_peças.grid(row=7, column=1, padx=10, pady= 7, sticky='nswe', columnspan = 2)
################### Caixa seleção SERVIÇOS
descrição_serviço = tk.Label(text='Serviços fornecidos: ') 
descrição_serviço.grid(row=8, column=0)
combobox_selecionar_serviços = ttk.Combobox(values=lista_serviços)
combobox_selecionar_serviços.grid(row=8, column=1, padx=10, pady= 7, sticky='nswe', columnspan = 2)

#################################### SOMA TOTAL ############################################
tt = tk.Label(text='Valor total: R$')
tt.grid(row=9, column=0, padx=10, pady= 7, sticky='nswe', columnspan = 2)
tt = tk.Entry()
tt.grid(row=9, column=1, padx=10, pady= 7, sticky='nswe', columnspan = 2)



#Seleção de Serviços;
""" result_btn = tk.Checkbutton(text="Selecionde a opção: ")
result_btn.grid(row=22, column=0, padx=10, pady= 7, sticky='nswe', columnspan = 1) """
serv1 = tk.Checkbutton(text='Opção 1')
serv1.grid(row=10, column=0, padx=10, pady= 7, sticky='nswe', columnspan = 1)
serv2 = tk.Checkbutton(text='Opção 2')
serv2.grid(row=11, column=0, padx=10, pady= 7, sticky='nswe', columnspan = 1)
serv3 = tk.Checkbutton(text='Opção 3')
serv3.grid(row=10, column=1, padx=10, pady= 7, sticky='nswe', columnspan = 2)
serv4 = tk.Checkbutton(text='Opção 4')
serv4.grid(row=11, column=1, padx=10, pady= 7, sticky='nswe', columnspan = 2) 

            
############### BOTÕES #########################
btn = tk.Button(text = 'Salvar', bd = '2')
btn.grid(row=12, column=0, padx=10, pady= 7, sticky='nswe', columnspan = 3) 
btn_salv = tk.Button(text = 'Salvar em PDF', bd = '2')
btn_salv.grid(row=13, column=0, padx=10, pady= 7, sticky='nswe', columnspan = 3) 


janela.mainloop()
