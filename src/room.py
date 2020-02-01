"""The Room object describes one lift room, containing one car.

A room contains sensors and its call buttons, outside of the car.
A room crosses defined floors

"""
from graphics_constants import FLOOR_HEIGHT, ROOM_WIDTH, CAR_WIDTH, CAR_ANIMATION_PIXELS_PER_STEP
from lift_system_constants import FLOOR_NUMBER

from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang.builder import Builder


Builder.load_file('room.kv')


class Room(Widget):

    car_pos_y = NumericProperty(0)
    car_width = NumericProperty(CAR_WIDTH)

    room_width = NumericProperty(ROOM_WIDTH)

    floor_number = NumericProperty(FLOOR_NUMBER)
    floor_height = NumericProperty(FLOOR_HEIGHT)

    controller = ObjectProperty(None)

    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        with self.canvas.after:
            Color(1, 1, 1, 1, mode='rgba')
            for y in range(self.floor_number + 1):
                Line(points=[0, y * self.floor_height, self.room_width, y * self.floor_height], dash_length=5, dash_offset=5)

    def attach_controller(self, controller):
        self.controller = controller

    @property
    def car_max_y(self):
        return self.floor_height * self.floor_number - self.car_width

    def move_car_step_up(self):
        new_y = self.car_pos_y + CAR_ANIMATION_PIXELS_PER_STEP
        if new_y <= self.car_max_y:
            self.car_pos_y = new_y

    def move_car_step_down(self):
        new_y = self.car_pos_y - CAR_ANIMATION_PIXELS_PER_STEP
        if new_y >= 0:
            self.car_pos_y = new_y
