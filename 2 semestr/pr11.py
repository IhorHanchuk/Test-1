from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, name="main"):
        super().__init__(name=name)
        layout = BoxLayout()
        
        btn4 = Button(text="4", on_press=self.switch_to_screen_4)
        btn2 = Button(text="2", on_press=self.switch_to_screen_2)
        btn3 = Button(text="3", on_press=self.switch_to_screen_3)
        btn1 = Button(text="1", on_press=self.switch_to_screen_1)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        
        self.add_widget(layout)

    def switch_to_screen_1(self, instance):
        self.manager.current = '1'

    def switch_to_screen_2(self, instance):
        self.manager.current = '2'

    def switch_to_screen_3(self, instance):
        self.manager.current = '3'

    def switch_to_screen_4(self, instance):
        self.manager.current = '4'

class Screen1(Screen):
    def __init__(self, name="1"):
        super().__init__(name=name)
        layout = BoxLayout()
        back_btn = Button(text="Back", on_press=self.switch_back)
        slider = Slider(min=4, max=1000, value=20)
        input = TextInput()
        layout.add_widget(slider)
        layout.add_widget(input)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class Screen2(Screen):
    def __init__(self, name="2"):
        
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal') 
        back_btn = Button(text="Back", on_press=self.switch_back)
        checkBox = CheckBox()
        self.txt = Label(text="Натисни:")
        layout.add_widget(self.txt)  
        layout.add_widget(checkBox)
        layout.add_widget(back_btn) 
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class Screen3(Screen):
    def __init__(self, name="3"):
        super().__init__(name=name)
        layout = BoxLayout()
        back_btn = Button(text="Back", on_press=self.switch_back)
        progressBar = ProgressBar(max=10)
        switch = Switch()
        layout.add_widget(switch)
        layout.add_widget(progressBar)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class Screen4(Screen):
    def __init__(self, name="4"):
        super().__init__(name=name)
        layout = BoxLayout()
        scroll_view = ScrollView()
        content = BoxLayout(orientation='vertical')
        for i in range(1):
            label = Label(text="Dark label".format(i+1))
            content.add_widget(label)
        scroll_view.add_widget(content)
        back_btn = Button(text="Back", on_press=self.switch_back)
        togglebutton = ToggleButton(text='Натисни', group='toggles', state='normal')
    
        layout.add_widget(scroll_view)
        layout.add_widget(togglebutton)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main_screen = MainScreen()
        screen_1 = Screen1()
        screen_2 = Screen2()
        screen_3 = Screen3()
        screen_4 = Screen4()

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(screen_1)
        screen_manager.add_widget(screen_2)
        screen_manager.add_widget(screen_3)
        screen_manager.add_widget(screen_4)

        return screen_manager

MyApp().run()
