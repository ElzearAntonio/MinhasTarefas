from kivymd.uix.screen import MDScreen

from kivy.uix.popup import Popup
from kivy.uix.label import Label


class LoginScreen(MDScreen):
    def ir_para_tela_tarefas(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        confirmar_senha = self.ids.confirmar_senha.text

        # Verifica se senha e confirmar_senha são iguais
        if senha == confirmar_senha and senha != "":
            self.manager.current = 'tela2'
        else:
            self.show_popup_error()

        # Limpa os campos
        self.ids.usuario.text = ''
        self.ids.senha.text = ''
        self.ids.confirmar_senha.text = ''

    def show_popup_error(self):
        popup_content = Label(text="Usuário ou senha incorreta")

        popup = Popup(title="Erro",
                      content=popup_content,
                      size_hint=(None, None),
                      size=(400, 400))
        popup.open()