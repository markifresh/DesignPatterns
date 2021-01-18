############# Main app class ##################
class DirectionService:
    def __init__(self):
        self.travel_mode = None

    def get_eta(self):
        return self.travel_mode.get_eta()

    def get_direction(self):
        return self.travel_mode.get_direction()

    def get_travel_mode(self):
        return self.travel_mode

    def set_travel_mode(self, travel_object):
        self.travel_mode = travel_object


############## Interface ########################
# Setting up interface for class DirectionService
from abc import ABC
class TravelMode(ABC):

    def get_eta(self):
        pass

    def get_direction(self):
        pass


############## Classes based on Interface ########
class Driving(TravelMode):
    def get_eta(self):
        print("Calculating ETA (driving)")
        return 1

    def get_direction(self):
        print("Calculating Direction (driving)")
        return 1


class Bicycling(TravelMode):
    def get_eta(self):
        print("Calculating ETA (bicycling)")
        return 2

    def get_direction(self):
        print("Calculating Direction (bicycling)")
        return 2

class Walking(TravelMode):
    def get_eta(self):
        print("Calculating ETA (walking)")
        return 3

    def get_direction(self):
        print("Calculating Direction (walking)")
        return 3

class Transit(TravelMode):
    def get_eta(self):
        print("Calculating ETA (transit)")
        return 4

    def get_direction(self):
        print("Calculating Direction (transit)")
        return 4


############# TESTING ##############
def driver():
    nav_app = DirectionService()
    nav_app.set_travel_mode(Walking())
    nav_app.get_eta()
    nav_app.get_direction()

    nav_app.set_travel_mode(Driving())
    nav_app.get_eta()
    nav_app.get_eta()
