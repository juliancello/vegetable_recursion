"""
Recursion with veggies
Inspired by a timelapse of me cutting up a pepper
All dimensions are using metric unless otherwise specified
"""
from abc import abstractmethod
from enum import Enum
from typing import TypeVar, Mapping
from math import pi


class WeirdPeelException(BaseException):
    pass


class Vegetable(object):
    def __init__(self, length: int, diameter: int, skin: list, has_seeds: bool, is_hollow: bool, has_stem: bool,
                 has_base: bool):
        self.length = length
        self.diameter = diameter
        self.skin = skin
        self.has_seeds = has_seeds
        self.is_hollow = is_hollow
        self.has_stem = has_stem
        self.has_base = has_base # apparently the base of an onion is called an adventitious. Why??? Seems like too much work
        self.pieces = 1

    @abstractmethod
    def cut(self, part): # cut hierarchy is implemented in subclassses
        # self.pieces += 1
        pass

    @abstractmethod
    def chop(self): # this and the next two methods depend on
        pass

    @abstractmethod
    def dice(self):
        pass

    @abstractmethod
    def mince(self):
        pass

    def peel(self):
        if "smooth" and "thin" not in self.skin:
            self.skin = None
        else:
            raise WeirdPeelException


class BellPepper(Vegetable):
    """
    Chop:
    Cut top, remove seeds, cut into wedges 1 cm wide, cut those into pieces 1cm x 1cm

    Dice:
    Chop, then cut each piece until it is no larger than 0.5 cm x 0.5 cm

    Mince:
    Dice, then cut each piece until it is no larger than 0.0625 cm x 0.0625 cm

    """
    def __init__(self, length, diameter):  # 11, 7
        super(BellPepper, self).__init__(length=length, diameter=diameter, skin=["smooth", "thin"], has_seeds=True,
                                         is_hollow=True, has_stem=True, has_base=True)

    def cut(self, part):
        pass

    def chop(self):
        """Cut top, remove seeds, cut base, cut into wedges 1 cm wide, cut those into pieces 1cm x 1cm"""
        self.has_stem = False # Cut top
        self.has_seeds = False # remove seeds
        self.has_base = False # cut base
        # cut into wedges <= 1 cm wide
        circumference = pi * self.diameter # figure out circumference
        # for i in range(circumference.__round__()

        # cut those into pieces 1cm x 1cm

    def dice(self):
        pass

    def mince(self):
        pass


class Carrot(Vegetable):
    """
    Chop:
    Peel, cut top, cut base, cut into pieces 0.1 cm thick

    Dice:
    Chop, then cut each piece until its radius is no larger than 1.5 cm

    Mince:
    Dice, then cut each piece into 8

    """
    def __init__(self, length, diameter): # 14, 3
        super(Carrot, self).__init__(length=length, diameter=diameter, skin=["rough", "thin"], has_seeds=False,
                                     is_hollow=False, has_stem=True, has_base=True)

    def cut(self, part):
        pass

    def chop(self):
        pass

    def dice(self):
        pass

    def mince(self):
        pass


class Onion(Vegetable):
    """
    Wait, the french method isn't recursive

    Chop:
    Cut in half, peel, make cuts .7 cm wide from base to stem, make cuts perpendicular from previous cuts .7 cm wide

    Dice:
    Chop

    Mince:
    Dice, then cut each piece into 8

    """
    def __init__(self, length, diameter):  # 7, 7
        super(Onion, self).__init__(length=length, diameter=diameter, skin=["smooth", "thick"], has_seeds=False,
                                     is_hollow=False, has_stem=True, has_base=True)

    def cut(self, part):
        pass

    def chop(self):
        pass

    def dice(self):
        pass

    def mince(self):
        pass


class Graveyard():
    pass
    # _length = 0
    # _width = 0
    # _height = 0

    # @property
    # def length(self):
    #     return self._length
    #
    # @length.setter
    # def length(self, value):
    #     self.length = value
    #
    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, value):
    #     self.width = value
    #
    # @property
    # def height(self):
    #     return self._height
    #
    # @height.setter
    # def height(self, value):
    #     self.height = value
