# High Scores

scores = []

choice = None

while choice != "0":

    print (
    """
    High Scores

    0 - Exit
    1 - Show Scores
    2 - Add a Acore
    3 - Delete a Score
    4 - Sort Scores

    """
    )

    choice = input(" Choice: ")
    print()

# exit
if choice == "0":
    print("Goodbye")