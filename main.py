from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList


Window.size = (350, 600)

#Window.fullscreen = True


class HowToWin10(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    class ContentNavigationDrawer(BoxLayout):
        pass
    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        # Set App Title
        self.title = "INTRO TO WINDOWS 10"

        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Light"

        screen_manager.add_widget(Builder.load_file("splashScreen.kv"))
        screen_manager.add_widget(Builder.load_file("mainScreen.kv"))

        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)  # Delay for 10 seconds


    def change_screen(self, dt):
        screen_manager.current = "MainScreen"



HowToWin10().run()