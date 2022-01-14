from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen, ScreenManager
import math
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDThemePicker
from kivy.config import Config
Config.set('graphics', 'resizable', True)


class ScreenManager(ScreenManager):
    pass

class MainScreen(Screen):
    
    pass

class Screen1(Screen):
    def limpar(self):
        self.ids.rms.text = ''
        self.ids.impedancia.text = ''
        self.ids.result_total_volt.text = ''

    def calcular_voltagem(self):
        self.dialog = MDDialog(
            title = "Ops, Algo Errado!",
            text = 'Repita a Operação',
            buttons= [MDFlatButton(text='OK', on_release = self.liberar)]
        )
        try:
            vl_rms = int(self.ids.rms.text)
            vl_imp = int(self.ids.impedancia.text)
            total = vl_rms * vl_imp
            raiz = int(math.sqrt(total))
            self.ids.result_total_volt.text = f"Módulo manda {raiz} V"
        except:
            self.dialog.open()
        
    def liberar(self, obj):
        self.dialog.dismiss()

class Screen2(Screen):

    def limpar_2(self):
        self.ids.total_rms.text = ''
        self.ids.result_total_amp.text = ''
       
    def calcular_amp(self):
        self.dialog = MDDialog(
            title = "Ops, Algo Errado!",
            text = 'Repita a Operação',
            buttons= [MDFlatButton(text='OK', on_release = self.liberar)]
        )
        try:
            valor_bat = int(self.ids.total_rms.text)
            total = int(valor_bat / 20)
            self.ids.result_total_amp.text = f"Bateria Min. {total} Ampéres"
        except:
            self.dialog.open()
    
    def liberar(self, obj):
        self.dialog.dismiss()

class Screen3(Screen):
    def limpar_3(self):
        self.ids.rms.text = ''
        self.ids.impedancia.text = ''
        self.ids.result_total_volt.text = ''

    def calcular_voltagem(self):
        self.dialog = MDDialog(
            title = "Ops, Algo Errado!",
            text = 'Repita a Operação',
            buttons= [MDFlatButton(text='OK', on_release = self.liberar)]
        )
        try:
            vl_rms = int(self.ids.rms.text)
            vl_imp = int(self.ids.impedancia.text)
            total = vl_rms * vl_imp
            raiz = int(math.sqrt(total))
            self.ids.result_total_volt.text = f"Aplicar até {raiz} V"
        except:
            self.dialog.open()
        
    def liberar(self, obj):
        self.dialog.dismiss()


class Screen_ajuda(Screen):
    pass

class MyApp(MDApp):
    

    def build(self):
        self.title = "Calculadora de Potência"
        self.icon = 'icon.png'
        #Window.size = (1080, 2400)
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_palette = "Purple"  # "Green", "Red"

        

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Tema",
                "height": dp(56),
                "on_release": lambda x=f"Tema": self.show_theme_picker(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "FAQ",
                "height": dp(56),
                "on_release": lambda x=f"FAQ": self.help_callback(x)
            },
            {
                "viewclass": "TwoLineListItem",
                "icon": 'weight-kilogram',
                "text": "Fechar",
                "height": dp(56),
                "on_release": lambda x=f"Fechar": self.menu_callback(x)
            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
        )

        return Builder.load_file('main.kv')

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()
        self.stop()

    def help_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()
        self.root.current = 'ajuda'

    def show_theme_picker(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    

if __name__ == "__main__":
    MyApp().run()
