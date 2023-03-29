from itertools import permutations

from modules import logging
from modules import config
from modules import midi_functions
from modules import theory


if __name__ == '__main__':
    # Initialize logger and parse config
    logger = logging.initialize_logger()
    args = config.parse_args()
    if args['logLevel'] is not None:
        logger.setLevel(args['logLevel'])
    
    octave_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    #octave_notes = ['C']

    for i in octave_notes:
        progressions = theory.get_progression_sequence()
        for chord_progression in progressions:
            mode = theory.IONIAN(i, chord_progression)

            chord_progression_letters, chord_progression_midi = mode.generate_progression()
            
            file_suffix = '-'.join(chord_progression)
    
            midi_functions.testmidi(chord_progression_midi, f'{i}-IONIAN-{file_suffix}.mid')
