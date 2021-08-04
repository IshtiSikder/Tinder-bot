import os
import csv

class SessionData:

    def __init__(self, user, password, start):
        self.user             = user
        self.password         = password
        self.start            = start
        self.left_swipes      = 0
        self.right_swipes     = 0
        self.total_swipes     = 0
        self.matches          = 0
        self.duration_seconds = 0.0
    
    def get_summary(self):
        return [self.user, 
                self.start.strftime("%x"),
                self.start.strftime("%X"), 
                self.left_swipes, 
                self.right_swipes, 
                self.total_swipes,
                self.matches, 
                self.duration_seconds]
               
    def to_csv(self, filepath):
        if (os.path.isfile(filepath)):
            with open(filepath, "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(self.get_summary())
        else:
            with open(filepath, "w") as csv_file:
                header = ["User", 
                          "Date", 
                          "Time", 
                          "Left Swipes", 
                          "Right Swipes", 
                          "Total Swipes",
                          "Matches", 
                          "Duration (seconds)"]
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(header)
                csv_writer.writerow(self.get_summary())
