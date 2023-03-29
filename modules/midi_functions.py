from midiutil.MidiFile import MIDIFile

def testmidi(progression: list, outfile: str):
    # create MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 80)
    
    # add some notes
    channel = 0
    volume = 100

    for i in range(len(progression)):
        for note in progression[i]:
            pitch = note           
            duration = 4   # 8 beat long
            mf.addNote(track, channel, pitch, time, duration, volume)
        time += 4

    # write it to disk
    with open(f'output/{outfile}', 'wb') as outf:
        mf.writeFile(outf)