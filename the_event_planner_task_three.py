#Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

attendees = input("Enter number of attendees: ")
venue = "large hall," if int(attendees) > 100 else "conference room,"
music = "audio system," if int(attendees) > 100 else "iPhone speaker,"
visual = "projector." if int(attendees) > 100 else "laptop."
print("For a hall we reccomend a", venue, "for music we reccomend an", music, "and for visual we reccomend a", visual)
print("We Reccomend Veggie Delight Caterers") if input("Do you want vegetarian food?") == "yes" else print("We Reccomend Gourmet Meals Caterers")