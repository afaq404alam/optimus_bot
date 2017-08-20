import abc


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, subject):
        """Called when the observed object is
        modified. You call a Subject object's
        notify method to notify all the
        object's observers of the change."""
        pass
