import os
import json
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivy.uix.checkbox import CheckBox
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout


class RightCheckbox(IRightBodyTouch, CheckBox):
    '''CheckBox que pode ser colocado à direita do item da lista.'''
    pass

lsttarefas = []
tarefasmd = []

class TarefasScreen(MDScreen):
    def adicionar_tarefas(self):
        tarefa = self.ids.addtarefa
        texto_tarefa = tarefa.text.strip()
        prioridade = self.ids.prioridade_tarefa.text

        if texto_tarefa:
            # Criar o item da lista com suporte a widget na direita
            texto_tarefa += ' (Prioridade: ' +prioridade+ ')'
            nova_tarefa = OneLineAvatarIconListItem(text=texto_tarefa)
            tarefasmd.append(nova_tarefa)
            global lsttarefas
            lsttarefas.append(texto_tarefa)
            # Criar e adicionar o CheckBox
            checkbox = RightCheckbox()
            nova_tarefa.add_widget(checkbox)

            # Adicionar o item à lista
            self.ids.lista_tarefas.add_widget(nova_tarefa)

            # Limpar o campo de texto
            tarefa.text = ""

    def carregar_tarefas(self):
        try:
            global lsttarefas
            global tarefasmd
            # Tentar abrir o arquivo de tarefas
            with open('tarefas.json', 'r') as f:
                tarefas = json.load(f)

                # Adicionar as tarefas carregadas à lista
                for tarefa_texto in tarefas:
                    nova_tarefa = OneLineAvatarIconListItem(text=tarefa_texto)
                    tarefasmd.append(nova_tarefa)
                    lsttarefas.append(tarefa_texto)
                    checkbox = RightCheckbox()
                    nova_tarefa.add_widget(checkbox)
                    self.ids.lista_tarefas.add_widget(nova_tarefa)
        except FileNotFoundError:
            # Se o arquivo não existir, não faz nada
            pass


    def voltar_tela(self):
        self.manager.current = 'tela1'

    def deletar_tarefas(self):
        global tarefasmd, lsttarefas

        # Remover visualmente da lista
        for item in tarefasmd:
            self.ids.lista_tarefas.remove_widget(item)

        # Limpar as listas internas
        tarefasmd.clear()
        lsttarefas.clear()

        # Apagar o arquivo JSON
        if os.path.exists("tarefas.json"):
            os.remove("tarefas.json")

    def on_pre_enter(self):
        # Carregar as tarefas ao entrar na tela
        self.carregar_tarefas()

def salvar_tarefas():
    # Obter todos os textos dos itens da lista (somente os itens do tipo OneLineAvatarIconListItem)
    # Salvar as tarefas em um arquivo JSON
    with open('tarefas.json', 'w') as f:
        json.dump(lsttarefas, f)