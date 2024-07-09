def get_user_selection(devices, device_type):
    while True:
        try:
            choice = int(input(f"Select a {device_type} by number: ")) - 1
            if 0 <= choice < len(devices):
                return devices[choice]
            else:
                print(f"Please enter a number between 1 and {len(devices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
