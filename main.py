import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import sqlite3



class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window_config()
        self.tela_principal()


    def window_config(self):
        self.geometry("500x600")
        self.resizable(False, False)


    def cadastrar_produto(self):

        with sqlite3.connect('produtos.db') as conexao:
            db = conexao.cursor()

            db.execute('create table if not exists produtos(Codigo do Produto text, Nome do Produto text, Descrição do Produto text, Valor do Produto text, Tipo do Produto text);')

            self.codigo_produto = self.codigo_produto_entry.get()
            self.nome_produto = self.nome_produto_entry.get()
            self.descricao_produto = self.descricao_produto_entry.get()
            self.valor_produto = self.valor_produto_entry.get()
            self.tipo_produto = self.tipo_do_produto_opt.get()

            db.execute('insert into produtos values(?,?,?,?,?)', [self.codigo_produto, self.nome_produto, self.descricao_produto, self.valor_produto, self.tipo_produto])
            conexao.commit()

            messagebox.showinfo('Sucesso', f'{self.nome_produto} Foi cadastrado com sucesso!')



    def tela_principal(self):

        self.codigo_produto = StringVar()
        self.nome_produto = StringVar()
        self.descricao_produto = StringVar()
        self.valor_produto = StringVar()


        self.codigo_produto_label = ctk.CTkLabel(self, text='Código do Produto: ', font=('arial bold', 20))
        self.nome_produto_label = ctk.CTkLabel(self, text='Nome do Produto: ', font=('arial bold', 20))
        self.descricao_produto_label = ctk.CTkLabel(self, text='Desc. do Produto: ', font=('arial bold', 20))
        self.valor_produto_label = ctk.CTkLabel(self, text='Valor do Produto: ', font=('arial bold', 20))
        self.tipo_do_produto_label = ctk.CTkLabel(self, text='Tipo do Produto: ', font=('arial bold', 20))

        self.codigo_produto_entry = ctk.CTkEntry(self, width=240, height=35, textvariable=self.codigo_produto)
        self.nome_produto_entry = ctk.CTkEntry(self, width=240, height=35, textvariable=self.nome_produto)
        self.descricao_produto_entry = ctk.CTkEntry(self, width=240, height=35, textvariable=self.descricao_produto)
        self.valor_produto_entry = ctk.CTkEntry(self, width=240, height=35, textvariable=self.valor_produto)
        self.tipo_do_produto_opt = ctk.CTkOptionMenu(self, values=['Alimentos', 'Informática', 'Eletrônicos'], width=240, height=35, fg_color='grey', corner_radius=15)
        self.tipo_do_produto_opt.set('Selecione')

        self.botao_cadastrar = ctk.CTkButton(self, text='Cadastrar', font=('arial bold', 20), height=35, width=260, command=self.cadastrar_produto)


        # Posicionando as Labels
        self.codigo_produto_label.place(x = 40, y = 80)
        self.nome_produto_label.place(x = 40, y = 160)
        self.descricao_produto_label.place(x = 40, y = 240)
        self.valor_produto_label.place(x = 40, y = 320)
        self.tipo_do_produto_label.place(x = 40, y = 400)

        self.codigo_produto_entry.place(x = 220, y = 80)
        self.nome_produto_entry.place(x = 220, y = 160)
        self.descricao_produto_entry.place(x = 220, y = 240)
        self.valor_produto_entry.place(x = 220, y = 320)
        self.tipo_do_produto_opt.place(x = 220, y = 400)

        self.botao_cadastrar.place(x = 100, y = 500)


if __name__ == "__main__":
    app = App()
    app.mainloop()