from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivy.uix.checkbox import CheckBox
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout




class RightCheckbox(IRightBodyTouch, CheckBox):
    '''CheckBox que pode ser colocado à direita do item da lista.'''
    pass


class TarefasScreen(MDScreen):
    def adicionar_tarefas(self):
        tarefa = self.ids.addtarefa
        texto_tarefa = tarefa.text.strip()

        if texto_tarefa:
            # Criar o item da lista com suporte a widget na direita
            nova_tarefa = OneLineAvatarIconListItem(text=texto_tarefa)

            # Criar e adicionar o CheckBox
            checkbox = RightCheckbox()
            nova_tarefa.add_widget(checkbox)

            # Adicionar o item à lista
            self.ids.lista_tarefas.add_widget(nova_tarefa)

            # Limpar o campo de texto
            tarefa.text = ""