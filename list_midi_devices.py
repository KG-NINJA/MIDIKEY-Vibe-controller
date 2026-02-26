import mido

def list_devices():
    print("Available MIDI Input Ports:")
    inputs = mido.get_input_names()
    if not inputs:
        print("  None found.")
    else:
        for i, name in enumerate(inputs):
            print(f"  {i}: {name}")

    print("\nAvailable MIDI Output Ports:")
    outputs = mido.get_output_names()
    if not outputs:
        print("  None found.")
    else:
        for i, name in enumerate(outputs):
            print(f"  {i}: {name}")

if __name__ == "__main__":
    list_devices()
