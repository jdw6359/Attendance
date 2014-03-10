def record_brother(ID):
    print("Brother with ID: "+str(ID)+" in attendance")
    





def main():
    print("Event Starting\n")

    """
        attendees=["Woodward", "Kenny", "Fink"]
        for attendee in attendees:
            record_brother(attendee)
    """
    while(1):
        brother_id=input()
        record_brother(brother_id)

main()
