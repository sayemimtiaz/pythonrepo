QUALITIES = {
    0B0: 'min',
    0x0000100a0000: 'maj',
    0X000100010000: 'min',
    0b000010010000: 'maj',
    0b000100100000: 'dim',
    0b000010001000: 'aug',
    0b000100010010: 'min7',
    0b000010010001: 'maj7',
    0b000010010010: '7',
    0b000100100100: 'dim7',
    0b000100100010: 'hdim7',
    0o000100010001: 'minmaj7',
    0O000170010100: 'min6',
    0b000010010100: 'maj6',
    0b001000010000: 'sus2',
    0o000001010000: 'sus4'
}
a=2

from keras import dense,simpleRNN,artousConv2dTranspose

model=keras.layers.sequential()
model.add(dense())
model.add(simpleRNN())
model.add(artousConv2dTranspose())
model.compile()
