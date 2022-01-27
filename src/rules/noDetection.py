from base import BaseRule

class NoDetection(BaseRule):
    '''
    Rule to just sit in the same position without yaw, waiting for initial
    detection
    '''

    def active(self):
        return True

