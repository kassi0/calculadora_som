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

TEXT = """"""

KV = '''

ScreenManager:
    
    MainScreen:
    Screen1:
    Screen2:
    Screen3:
    Screen_ajuda:

<MainScreen>:
    name: "mainscreen"
    FloatLayout:

        MDToolbar:
            #md_bg_color: 1,1,0,0
            left_action_items: [["menu", lambda x: app.callback(x)]]
            title: "Calculadora de Potência"
            #specific_text_color: app.theme_cls.primary_color
            pos_hint: {'top': 1}
            elevation: 0

        Image:
            source: 'in.png'
            adaptive_height: True
            #size_hint: 0.6, 0.5
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        MDRectangleFlatButton:
            text: "VOLTAGEM MÓDULO"
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            #size_hint_x: .7
            #size_hint: None,None
            on_release:
                app.root.current = 'screen1'
                root.manager.transition.direction = 'left'
                

        MDRectangleFlatButton:
            text: "AMPERES NECESSÁRIOS"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            #size_hint_x: .7
            #size_hint: None,None
            on_release:
                app.root.current = 'screen2'
                root.manager.transition.direction = 'left'
        
        MDRectangleFlatButton:
            text: "VOLTAGEM FALANTE"
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            #size_hint_x: .7
            #size_hint: None,None
            on_release:
                app.root.current = 'screen3'
                root.manager.transition.direction = 'left'


<Screen1>:
    name: "screen1"
    FloatLayout:

        MDToolbar:
            #md_bg_color: 1,1,0,0
            left_action_items: [["menu", lambda x: app.callback(x)]]
            title: "Calcule Voltagem Aplicada"
            #specific_text_color: app.theme_cls.primary_color
            pos_hint: {'top': 1}
            elevation: 0
        
        Image:
            source: 'modulo.png'
            #size_hint: .5, .5
            adaptive_height: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}

        MDLabel:
         
            text: "Vamos calcular o quanto de voltagem seu módulo envia." 
            font_size: 60
            #color: '#00FF7F'
            halign: "center" 
            specific_text_color: app.theme_cls.primary_color  
            pos_hint: {"center_x": 0.5, "center_y": .85} 
        
        MDLabel:
            id: result_total_volt
            text: ''
            font_size: 70
            color: '#00FF7F'
            halign: "center"
            multiline: False
            pos_hint: {"center_x": .5, "center_y": .4}            
        
        MDTextField:
            id: rms
            hint_text: "Potencia em RMS do Amplificador"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Insira o Valor RMS do Amplificador"
            pos_hint: {"center_x": .5, "center_y": .7}
            size_hint_x: (0.8)
            icon_right: 'amplifier' #"arm-flex-outline"
            icon_right_color: app.theme_cls.primary_color
        
        MDTextField:
            id: impedancia
            hint_text: "Impedância"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Insira o Valor da Impedância"
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint_x: (0.8)
            icon_right: 'omega'
            icon_right_color: app.theme_cls.primary_color
        
        MDRectangleFlatButton:
            text: "Calcular"
            pos_hint: {'center_x': 0.4, 'center_y': 0.5}
            #size_hint_x: .7
            #size_hint: None,None
            on_press: root.calcular_voltagem()

        MDRectangleFlatButton:
            text: "Limpar"
            pos_hint: {'center_x': 0.65, 'center_y': 0.5}
            #size_hint_x: .7
            #size_hint: None,None
            on_press: root.limpar()

        MDFloatingActionButton:
            icon: "android"
            md_bg_color: app.theme_cls.primary_color
            icon: "arrow-left"
            icon_size: "200sp"
            pos_hint: {"center_x": .9, 'center_y' : .09}
            on_press:
                setattr(root.manager, 'current', 'mainscreen')
                root.manager.transition.direction = 'right'
                root.limpar()
        

<Screen2>:
    name: "screen2"
    FloatLayout:

        MDToolbar:
            
            #md_bg_color: 1,1,0,0
            left_action_items: [["menu", lambda x: app.callback(x)]]
            #left_action_items: [["arrow-left", lambda _: setattr(root.manager, 'current', 'mainscreen')]]
            title: "Calcule Amperes Necessários"
            #specific_text_color: app.theme_cls.primary_color
            pos_hint: {'top': 1}
            elevation: 0
       
        Image:
            source: 'bateria.png'
            #size_hint: .5, .5
            adaptive_height: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}

        MDLabel:
         
            text: "Calcule quantos ampéres de bateria necessita." 
            font_size: 60
            #color: '#00FF7F'
            halign: "center" 
            specific_text_color: app.theme_cls.primary_color  
            pos_hint: {"center_x": 0.5, "center_y": .85} 

        MDLabel:
         
            text: "Some a potência de todos os Módulos." 
            font_size: 60
            #color: '#00FF7F'
            halign: "center" 
            specific_text_color: app.theme_cls.primary_color  
            pos_hint: {"center_x": 0.5, "center_y": .8}
                
        MDLabel:
            id: result_total_amp
            text: ''
            font_size: 70
            color: '#00FF7F'
            halign: "center"
            multiline: False
            pos_hint: {"center_x": .5, "center_y": .4}

        MDTextField:
            id: total_rms
            hint_text: "Total em RMS dos Módulos"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Insira o Valor total dos Módulos"
            pos_hint: {"center_x": .5, "center_y": .7}
            size_hint_x: (0.8)
            icon_right: 'amplifier' #"arm-flex-outline"
            icon_right_color: app.theme_cls.primary_color

        MDRectangleFlatButton:
            text: "Calcular"
            pos_hint: {'center_x': 0.4, 'center_y': 0.5}
            #size_hint_x: .7
            #size_hint: None,None
            on_press: root.calcular_amp()

        MDRectangleFlatButton:
            text: "Limpar"
            pos_hint: {'center_x': 0.65, 'center_y': 0.5}
            #size_hint_x: .7
            #size_hint: None,None
            on_press: root.limpar_2()
        
        MDFloatingActionButton:
            icon: "android"
            md_bg_color: app.theme_cls.primary_color
            icon: "arrow-left"
            icon_size: "200sp"
            pos_hint: {"center_x": .9, 'center_y' : .09}
            on_press:
                setattr(root.manager, 'current', 'mainscreen')
                root.manager.transition.direction = 'right'
                root.limpar_2()
        
                
<Screen3>:
    name: "screen3"
    FloatLayout:

        MDToolbar:
            #md_bg_color: 1,1,0,0
            left_action_items: [["menu", lambda x: app.callback(x)]]
            title: "Voltagem Suportada"
            #specific_text_color: app.theme_cls.primary_color
            pos_hint: {'top': 1}
            elevation: 0
        
        Image:
            source: 'falante.png'
            #size_hint: .5, .5
            adaptive_height: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        
        MDLabel:
            id: result_total_volt
            text: ''
            font_size: 70
            color: '#00FF7F'
            halign: "center"
            multiline: False
            pos_hint: {"center_x": .5, "center_y": .4}
         
        MDLabel:
         
            text: "Vamos calcular o quanto de voltagem seu falante vai suportar." 
            font_size: 60
            #color: '#00FF7F'
            halign: "center" 
            specific_text_color: app.theme_cls.primary_color  
            pos_hint: {"center_x": 0.5, "center_y": .85}           
        
        MDTextField:
            id: rms
            hint_text: "Potencia em RMS do Falante"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Insira o Valor RMS do Falante"
            pos_hint: {"center_x": .5, "center_y": .7}
            size_hint_x: (0.8)
            icon_right: 'amplifier' #"arm-flex-outline"
            icon_right_color: app.theme_cls.primary_color
        
        MDTextField:
            id: impedancia
            hint_text: "Impedância"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Insira o Valor da Impedância"
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint_x: (0.8)
            icon_right: 'omega'
            icon_right_color: app.theme_cls.primary_color
        
        MDRectangleFlatButton:
            text: "Calcular"
            pos_hint: {'center_x': 0.4, 'center_y': 0.5}
            #size_hint_x: .7
            #size_hint: None,None
            on_press: root.calcular_voltagem()

        MDRectangleFlatButton:
            text: "Limpar"
            pos_hint: {'center_x': 0.65, 'center_y': 0.5}
            #size_hint_x: .7
            #size_hint: None,None
            on_press: root.limpar_3()

        MDFloatingActionButton:
            md_bg_color: app.theme_cls.primary_color
            icon: "arrow-left"
            icon_size: "200sp"
            pos_hint: {"center_x": .9, 'center_y' : .09}
            on_press:
                setattr(root.manager, 'current', 'mainscreen')
                root.manager.transition.direction = 'right'
                root.limpar_3()
        


<Screen_ajuda>:
    name: 'ajuda'
    
    FloatLayout:

        MDToolbar:
            
            #md_bg_color: 1,1,0,0
            left_action_items: [["menu", lambda x: app.callback(x)]]
            #left_action_items: [["arrow-left", lambda _: setattr(root.manager, 'current', 'mainscreen')]]
            title: "FAQ"
            #specific_text_color: app.theme_cls.primary_color
            pos_hint: {'top': 1}
            elevation: 0

        MDLabel:

            text: '\\n' +\
                  '\\n' +\
                  'Bem vindo a calculadora de Potência Aplicada para Som Automotivo. Aqui vamos Calcular de Maneira rápida, o quanto de voltagem seu módulo envia, o quanto de voltagem seu Falante, Driver ou Twetter suporta e também o quanto de Ampéres de Bateria será necessário para suprir de forma mínima seu Sistema de som.'
            specific_text_color: app.theme_cls.primary_color 
            multiline: True 
            halign: "left" 
            font_size: '50'
            pos_hint: {"center_x": 0.5, "center_y": .8}
        
        MDLabel:

            text: '\\n' +\
                  '\\n' +\
                  'Contato: kassio.info@gmail.com'
            specific_text_color: app.theme_cls.primary_color 
            multiline: True 
            halign: "left" 
            font_size: '50'
            pos_hint: {"center_x": 0.5, "center_y": .44}

        MDRoundFlatIconButton:
            icon: "github"
            text: "GitHub"
            halign: "center"
            pos_hint: {'center_x': 0.65, 'center_y': 0.27}
            #size_hint_x: (0.5)
            #size_hint: None,None
            on_release:
                import webbrowser
                webbrowser.open('https://github.com/kassi0/')

        MDRoundFlatIconButton:
            icon: "coffee"
            text: "Me Pague um Lanche"
            halign: "center"
            pos_hint: {'center_x': 0.35, 'center_y': 0.27}
            #size_hint_x: (0.5)
            #size_hint: None,None
            on_release:
                import webbrowser
                webbrowser.open('https://mpago.la/1KByM4D')
        
        MDFloatingActionButton:
            icon: "android"
            md_bg_color: app.theme_cls.primary_color
            icon: "arrow-left"
            icon_size: "200sp"
            pos_hint: {"center_x": .9, 'center_y' : .09}
            on_press:
                setattr(root.manager, 'current', 'mainscreen')
                root.manager.transition.direction = 'right'



'''

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

        return Builder.load_string(KV)
        #return Builder.load_file('app.kv')

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
