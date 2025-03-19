#! /usr/bin/env python3

from running import Running
from cycling import Cycling
from datetime import datetime

def get_valid_time(prompt):
    while True:
        time_str = input(prompt)
        try:
            return datetime.strptime(time_str, "%H:%M")
        except ValueError:
            print("Invalid time format! Please enter in HH:MM format.")

def main():
    while True:
        print("\nChoose a workout type:")
        print("1. Running")
        print("2. Cycling")
        print("3. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "3":
            print("Goodbye!")
            break
        
        if choice not in ["1", "2"]:
            print("Invalid choice. Please try again.")
            continue
        
        start_time = get_valid_time("Enter start time (HH:MM): ")
        end_time = get_valid_time("Enter end time (HH:MM): ")

        while end_time <= start_time:
            print("End time must be after start time. Please re-enter.")
            end_time = get_valid_time("Enter end time (HH:MM): ")

        heart_rate = int(input("Enter average heart rate (bpm): "))
        distance = float(input("Enter distance covered (km): "))
        
        if choice == "1":
            workout = Running(start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), heart_rate, distance)
        else:
            workout = Cycling(start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), heart_rate, distance)
        
        print("\n" + workout.get_summary())

if __name__ == "__main__":
    main()
