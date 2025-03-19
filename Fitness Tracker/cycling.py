from workout import Workout

class Cycling(Workout):
    def calculate_speed(self):
        return self.distance / self.get_duration()
    
    def get_summary(self):
        return (f"Cycling Workout:\nDuration: {self.get_duration():.2f} hours\n"
                f"Distance: {self.distance} km\nSpeed: {self.calculate_speed():.2f} km/h\n"
                f"Heart Rate: {self.heart_rate} bpm")
