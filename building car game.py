command = ""
started = False
while command != 'quit':
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Its already started")
        else:
            started = True
            print("Car Started....")
    elif command == 'stop':
        if not started:
            print("Its Already stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == 'help':
        print("""
        Start = Car Started...
        Stop = Car Stopped
        Quit = to Quit
        """)
    elif command == 'quit':
        break
    else:
        print("Command Invalid!!!")
