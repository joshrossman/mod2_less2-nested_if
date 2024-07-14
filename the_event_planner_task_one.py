#2. Quick Decisions: The Event Planner 🎉
#Objective: To practice the use of shorthand if statements.
# Task 1: Code Correction You are provided with a Python script that is 
# supposed to help in event planning, but it has errors. Identify and fix them.
# Buggy Code:
# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)