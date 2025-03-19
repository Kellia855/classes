from workout import Workout

class Running(Workout):
    def calculate_speed(self):
        return self.distance / self.get_duration()
    
    def calculate_pace(self):
        return self.get_duration() * 60 / self.distance  # Minutes per unit distance
    
    def get_summary(self):
        return (f"Running Workout:\nDuration: {self.get_duration():.2f} hours\n"
                f"Distance: {self.distance} km\nSpeed: {self.calculate_speed():.2f} km/h\n"
                f"Pace: {self.calculate_pace():.2f} min/km\nHeart Rate: {self.heart_rate} bpm")
