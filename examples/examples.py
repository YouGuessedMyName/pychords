from pychords import *

def input_root():
    while True:
        print("Give me a root note")
        try:
            return REVERSED_CONCRETE_NOTE_NAMES[input()]
        except KeyError:
            print("I don't know that root")

def input_mode():
    print("What mode would you like?\n1) Major mode \n2) Natural minor mode")
    while True:
        num = input()
        if num == "1":
            return MAJOR_MODE
        if num == "2":
            return NATURAL_MINOR_MODE
        else:
            print("Is it really that difficult???")

def input_chord_type():
    print("What chord type would you like?\n1) Major chord 2) minor chord")
    while True:
        num = input()
        if num == "1":
            return MAJOR_CHORD
        if num == "2":
            return MINOR_CHORD
        else:
            print("Is it really that difficult???")
            
def main():
    print("First determine a scale!")
    scale = ConcreteScale(input_root(), input_mode())
    print("Now we have the following scale:")
    print(str(scale))
    
    print("Now lets transpose a chord from your scale into the key of Ab!")
    AbM = ConcreteScale(CN.GS, MAJOR_MODE)
    chord = ConcreteChord(input_root(), input_chord_type())
    print("Now we have the following chord:")
    print(str(chord))
    
    print(f"If we transpose {chord.short_representation()} from {scale.short_representation()} to {AbM.short_representation()}, we get:")
    transposed_chord = transpose_from_to_scale(chord, scale, AbM)
    print(str(transposed_chord))

    

if __name__ == "__main__":
    main()