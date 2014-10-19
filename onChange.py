__author__ = 'guney'

#call callback function when value changed
class OnChangeClass(object):

    def __init__(self,callback):
        self._value = 0
        self.callback = callback

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        new_value = int(new_value)
        if new_value!= self._value:
            self.callback(new_value)
        self._value = new_value

class OnChangeClass2(object):
    def __init__(self,callback):
        self._value = None
        self.callback = callback

    def value_getter(self):
        return self._value

    def value_setter(self, new_value):
        if self._value != new_value:
            self.callback()
        self._value = new_value

    def value_setter(self, new_value):
        if self._value != new_value:
            self.callback()
        self._value = new_value

    value = property(value_getter, value_setter)
