# The notes in a 12 note octave
octave_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
major_circle = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']
minor_circle = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F', 'C', 'G', 'D']

class IONIAN: # Defines the circle of fifths for the Ionian mode (Major)
    def __init__(self, root_note: str, chord_progression: list):
        self.root_note = root_note
        self.chord_progression = chord_progression

    def supertonic(self) -> str:
        root_note = self.root_note
        I_index = major_circle.index(root_note)
        II_index = (I_index - 1) % len(minor_circle)
        II = minor_circle[II_index]
        return II 

    def mediant(self) -> str:
        root_note = self.root_note
        I_index = major_circle.index(root_note)
        III_index = (I_index + 1) % len(minor_circle)
        III = minor_circle[III_index]
        return III

    def subdominant(self) -> str:
        root_note = self.root_note
        I_index = major_circle.index(root_note)
        IV_index = (I_index + 1) % len(major_circle)
        IV = major_circle[IV_index]
        return IV

    def dominant(self) -> str:
        root_note = self.root_note
        I_index = major_circle.index(root_note)
        V_index = (I_index - 1) % len(major_circle)
        V = major_circle[V_index]
        return V

    def submediant(self) -> str:
        root_note = self.root_note
        I_index = major_circle.index(root_note)
        VI = minor_circle[I_index]
        return VI
    
    def get_circle(self) -> dict:
        root_note = self.root_note
        
        # Get the chords from the circle of fifths
        I = major_chord(root_note)
        II = minor_chord(self.supertonic())
        III = minor_chord(self.mediant())
        IV = major_chord(self.subdominant())
        V = major_chord(self.dominant())
        VI = minor_chord(self.submediant())

        octave = 4
        # Convert the note values into MIDI note numbers
        Inum = [note_to_number(I[0], octave), note_to_number(I[1], octave), note_to_number(I[2], octave)]
        IInum = [note_to_number(II[0], octave), note_to_number(II[1], octave), note_to_number(II[2], octave)]
        IIInum = [note_to_number(III[0], octave), note_to_number(III[1], octave), note_to_number(III[2], octave)]
        IVnum = [note_to_number(IV[0], octave), note_to_number(IV[1], octave), note_to_number(IV[2], octave)]
        Vnum = [note_to_number(V[0], octave), note_to_number(V[1], octave), note_to_number(V[2], octave)]
        VInum = [note_to_number(VI[0], octave), note_to_number(VI[1], octave), note_to_number(VI[2], octave)]

        circle_letters = {'I' : I, 'II' : II, 'III' : III, 'IV' : IV, 'V' : V, 'VI' : VI}
        circle_midi = {'I' : Inum, 'II' : IInum, 'III' : IIInum, 'IV' : IVnum, 'V' : Vnum, 'VI' : VInum}
        return circle_letters, circle_midi
    
    def generate_progression(self) -> list:
        chord_progression = self.chord_progression
        circle_letters, circle_midi = self.get_circle()
        chord_progression_letters = [circle_letters[x] for x in chord_progression ]
        # print(chord_progression_letters)
        chord_progression_midi = [circle_midi[x] for x in chord_progression ]
        # print(chord_progression_midi)  

        return chord_progression_letters, chord_progression_midi

            



def minor_chord(note: str) -> list:
    root_index = octave_notes.index(note)
    minor_third = (root_index + 3) % len(octave_notes)
    major_third = (root_index + 7) % len(octave_notes)
    chord = [note, octave_notes[minor_third], octave_notes[major_third]]
    return chord

def major_chord(note: str) -> list:
    root_index = octave_notes.index(note)
    major_third = (root_index + 4) % len(octave_notes)
    minor_third = (root_index + 7) % len(octave_notes)
    chord = [note, octave_notes[major_third], octave_notes[minor_third]]
    return chord

def note_to_number(note: str, octave: int) -> int:
    notes_in_octave = len(octave_notes)
    note = octave_notes.index(note)
    note += (notes_in_octave * octave)
    assert 0 <= note <= 127
    return note

def get_progression_sequence():
    progressions = [
        ['I', 'IV', 'V'],
        ['I', 'II', 'V'],
        ['I', 'VI', 'II', 'V'],
        ['I', 'III', 'VI', 'II', 'V'],
        ['II', 'III', 'VI'],
        ['I', 'IV']
    ]
    return progressions

