from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('SimLiftHome.kv')


class SimLiftHome(BoxLayout):

    room = ObjectProperty(None)
    room_controller = ObjectProperty(None)

    def prepare(self):
        self.room.attach_controller(self.room_controller)
        self.room_controller.attach_room(self.room)

    def start(self):
        self.room_controller.run()

    def stop(self):
        self.room_controller.stop()


class SimLift(App):
    def build(self):
        sim_lift_home = SimLiftHome()
        sim_lift_home.prepare()
        return sim_lift_home


if __name__ == '__main__':
    SimLift().run()
