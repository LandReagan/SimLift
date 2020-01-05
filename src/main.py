from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

Builder.load_file('SimLiftHome.kv')


class ButtonUp(Button):
    pass


class ButtonDown(Button):
    pass


class MaintenancePanel(FloatLayout):

    parent = ObjectProperty(None)

    def change_floor(self, delta_floor):
        self.parent.change_floor(delta_floor)


class Car(Widget):
    pass


class Room(Widget):
    car = ObjectProperty(None)
    max_floor = 3


class SimLiftHome(Widget):
    room = ObjectProperty(None)
    maintenance_panel = ObjectProperty(None)
    car_floor = NumericProperty(0)

    def prepare(self):
        self.maintenance_panel.parent = self

    def change_floor(self, delta_floor):
        if 0 <= self.car_floor + delta_floor <= self.room.max_floor:
            self.car_floor += delta_floor

    def on_car_floor(self, *args):
        animation = Animation(duration=0.5, pos=(100, 100 + 100 * self.car_floor))
        animation.start(self.room.car)


class SimLift(App):
    def build(self):
        sim_lift_home = SimLiftHome()
        sim_lift_home.prepare()
        return sim_lift_home


if __name__ == '__main__':
    SimLift().run()
