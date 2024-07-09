import mido
from functions.get_user_selection import get_user_selection
from functions.jog_incremental import jog_incremental
from functions.list_midi_devices import list_midi_devices
from functions.rekordjog_start_sequence import rekordjog_start_sequence
from functions.tempo_reverse import tempo_reverse

def main():
    input_devices, output_devices = list_midi_devices()
    
    if input_devices:
        midi_inp_name = get_user_selection(input_devices, "Physical Controller")
    else:
        midi_inp_name = None
        print("No MIDI input devices found.")

    if output_devices:
        midi_out_name = get_user_selection(output_devices, "Emulated Controller")
    else:
        midi_out_name = None
        print("No MIDI output devices found.")
    return midi_inp_name, midi_out_name

if __name__ == "__main__":
    midi_inp_name, midi_out_name = main()

    if midi_inp_name and midi_out_name:
        with mido.open_input(midi_inp_name) as midi_inp, mido.open_output(midi_out_name) as midi_out:
            TURN_CLOCK_SPEED = 0x46
            TURN_COUNTER_SPEED = 0x3A
            PIONEER_PITCH_CONTROL = 0x70

            wheel_messages_counter = 3

            rekordjog_start_sequence()

            while True:
                ims = midi_inp.receive()
                if ims.type == 'control_change':
                    wheel_messages_counter = jog_incremental(ims, midi_out, wheel_messages_counter, TURN_CLOCK_SPEED, TURN_COUNTER_SPEED)
                    tempo_reverse(ims, midi_out, PIONEER_PITCH_CONTROL)

                if ims.type == 'note_on' or ims.type == 'note_off':
                    midi_out.send(mido.Message(ims.type, channel=ims.channel, note=ims.note, velocity=ims.velocity))
