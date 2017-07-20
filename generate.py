# Load LSTM network and generate text
import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from notes import *
from os import getcwd
from tools import *
import re

filename = "6-29489-0.2646.hdf5"




StudioGhibli = song2note(AlwaysWithMe)+song2note(CastleInTheSky)
raw_text = " ".join([str(i) for i in StudioGhibli])
# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)
# prepare the dataset of input to output pairs encoded as integers
seq_length = 20
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)
# define the LSTM model
model = Sequential()
model.add(LSTM(28, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.3))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
# load the network weights
model.load_weights("M:/Pyiano/model/" + filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
# pick a random seed
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print("Seed:")
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
# generate characters
generated = ""
for i in range(200):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	x = x / float(n_vocab)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = int_to_char[index]
	seq_in = [int_to_char[value] for value in pattern]
	generated += result
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print("\nDone.")
print("R:")
generated = re.sub(" +", " ", generated)
song = []
for num in [s for s in generated.split(" ")]:
	if len(num) == 0:
		continue
	if len(num) < 3:
		song.append(int(num))
	else:
		i = 0
		j = 2
		while j < len(num):
			if int(num[i:j]) < 49:
				song.append(int(num[i:j]))
			else:
				song.append(int(num[i]))
				song.append(int(num[i+1:j]))
			i += 1
			j += 1



Play(note2song(song))
