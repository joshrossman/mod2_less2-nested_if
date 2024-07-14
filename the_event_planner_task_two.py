#Task 2: Venue Selection
# Based on the corrected code from Task 1, 
# further enhance your code to recommend additional 
# things like "audio system" or "projector" 
# based on the number of attendees.

attendees = input("Enter number of attendees: ")
venue = "large hall," if int(attendees) > 100 else "conference room,"
music = "audio system," if int(attendees) > 100 else "iPhone speaker,"
visual = "projector." if int(attendees) > 100 else "laptop."
print("For a hall we reccomend a", venue, "for music we reccomend an", music, "and for visual we reccomend a", visual)