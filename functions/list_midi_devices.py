import mido

def list_midi_devices():
    input_devices = mido.get_input_names()
    output_devices = mido.get_output_names()

    print("\nPhysical Controller:")
    for i, device in enumerate(input_devices):
        print(f"{i + 1}: {device}")

    print("\nEmulated Controller:")
    for i, device in enumerate(output_devices):
        print(f"{i + 1}: {device}")

    return input_devices, output_devices