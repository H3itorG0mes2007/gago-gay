from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Login(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 50]
        self.spacing = 10  # Espaçamento entre os widgets

        # Título
        title_label = Label(text="MATBIT", font_size=40, color=(0, 0.7, 1, 1))
        self.add_widget(title_label)

        # Inputs de usuário e senha
        self.username_input = TextInput(hint_text="Nome de usuário", size_hint_y=None, height=40)
        self.password_input = TextInput(hint_text="Senha", password=True, size_hint_y=None, height=40)
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        # Botões
        self.login_button = Button(text="Entrar", background_color=(0, 0.7, 1, 1), size_hint_y=None, height=40)
        self.register_button = Button(text="Registrar", background_color=(0, 0.5, 0.1, 1), size_hint_y=None, height=40)
        self.add_widget(self.login_button)
        self.add_widget(self.register_button)


class MyApp(App):
    def build(self):
        return Login()


if __name__ == '__main__':
    MyApp().run()
