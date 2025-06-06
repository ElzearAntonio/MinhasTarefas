import os


from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

from screens.tarefas_screen.tarefasscreen import salvar_tarefas


# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
        os.path.join(os.getcwd(), "screens/tarefas_screen/tarefasscreen.kv")
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.login_screen.loginscreen",
        "TarefasScreen": "screens.tarefas_screen.tarefasscreen"
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        self.theme_cls.theme_style = 'Dark'
        return Factory.MainScreenManager()

    def on_stop(self):
        salvar_tarefas()


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()