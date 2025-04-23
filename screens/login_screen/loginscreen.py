from kivymd.uix.screen import MDScreen
from  kivymd.uix.toolbar import MDTopAppBar


class LoginScreen(MDScreen):
    def ir_para_tela_tarefas(self):
        self.manager.current = ('tela2')