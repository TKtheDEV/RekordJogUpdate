import configparser
import mido
from .clear_terminal import clear_terminal
def set_midi_devices():

    clear_terminal()

    input_devices = mido.get_input_names()
    for i, device in enumerate(input_devices, start=1):
        print(f"{i}. {device}")

    input_choice = int(input("Select your physical controller (enter number): ")) - 1
    selected_input = input_devices[input_choice] if 0 <= input_choice < len(input_devices) else None

    clear_terminal()

    output_devices = mido.get_output_names()
    for i, device in enumerate(output_devices, start=1):
        print(f"{i}. {device}")

    output_choice = int(input("Select DDJ-SX (emulated controller): ")) - 1
    selected_output = output_devices[output_choice] if 0 <= output_choice < len(output_devices) else None

    clear_terminal()

    config = configparser.ConfigParser()
    config['MIDI'] = {
        'input_device': selected_input,
        'output_device': selected_output,
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("MIDI devices have been saved to config.ini")

    return selected_input, selected_output
