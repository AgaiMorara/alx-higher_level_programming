#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            # Allow setting the 'first_name' attribute
            self.__dict__[name] = value
        else:
            raise AttributeError("object has no attribute.")