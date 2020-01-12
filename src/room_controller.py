from enum import Enum

from graphics_constants import CAR_ANIMATION_FPS

from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('room_controller.kv')


class Motor(Enum):
    UP = 1
    STOP = 2
    DOWN = 3


class RoomController(BoxLayout):

    room = ObjectProperty(None)

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.motor = Motor.STOP

    def attach_room(self, room):
        self.room = room

    def run(self):
        print('Room controller starts!')
        Clock.schedule_interval(self._control, 1.0/CAR_ANIMATION_FPS)

    def stop(self):
        print('Room controller stops!')
        Clock.unschedule(self._control)

    def set_motor_up(self):
        self.motor = Motor.UP

    def set_motor_down(self):
        self.motor = Motor.DOWN

    def _control(self, dt):
        if not self.room:
            return
        if self.motor == Motor.UP:
            self.room.move_car_step_up()
        elif self.motor == Motor.DOWN:
            self.room.move_car_step_down()
