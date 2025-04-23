from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList ,OneLineListItem

class TarefasScreen(MDScreen):
    def adicionar_tarefas(self):
        tarefa = self.ids.addtarefa
        texto_tarefa = self.ids.addtarefa.text.strip()

        if texto_tarefa:
            nova_tarefa = OneLineListItem(text = texto_tarefa)
            self.ids.lista_tarefas.add_widget(nova_tarefa)
            tarefa.text = ''