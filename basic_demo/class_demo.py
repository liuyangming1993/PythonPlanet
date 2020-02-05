#!/usr/bin/python
# coding:utf-8

"""类demo"""
__author__ = 'Liu Yangming'


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        print(self.lyrics)


pretty_boy = Song("Oh my pretty pretty ...")
pretty_boy.sing()

big_big_world = Song("I'm a big big ...")
big_big_world.sing()
