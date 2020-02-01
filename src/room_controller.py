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
    button_motor_up = ObjectProperty(None)
    button_motor_down = ObjectProperty(None)

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.motor = Motor.STOP

    def attach_room(self, room):
        self.room = room

    def run(self):
        """
        Starts the control loop of the room controller
        :return: Nothing
        """
        print('Room controller starts!')
        Clock.schedule_interval(self._control, 1.0/CAR_ANIMATION_FPS)

    def stop(self):
        """
        Stops the control loop of the room controller
        :return:
        """
        print('Room controller stops!')
        Clock.unschedule(self._control)

    def set_motor(self):
        if self.button_motor_up.state == 'down' and self.button_motor_down.state == 'normal':
            self.motor = Motor.UP
        elif self.button_motor_up.state == 'normal' and self.button_motor_down.state == 'down':
            self.motor = Motor.DOWN
        else:
            self.motor = Motor.STOP

    def _control(self, dt):
        """
        Control loop of the room controller. It (in turn):
        - Update sensors state,
        - Trigger the controller program,
        - Moves the Car one time step depending on Motor state.
        :param dt: delta time since last call, as it is triggered by the Kivy Clock
        :return: Nothing
        """
        if not self.room:
            return
        if self.motor == Motor.UP:
            self.room.move_car_step_up()
        elif self.motor == Motor.DOWN:
            self.room.move_car_step_down()
