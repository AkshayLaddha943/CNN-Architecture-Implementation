from keras.models import Sequential
from keras.layers import Conv2D, AveragePooling2D, Flatten, Dense

model = Sequential()

#C1 Convolutional layer
model.add(Conv2D(filters=6, kernel_size=5, strides=1, activation='tanh', input_shape=(28,28,1), padding='same'))

#S2 Pooling layer
model.add(AveragePooling2D(pool_size=2, strides=2, padding='valid'))

#C3 Convolutional layer
model.add(Conv2D(filters=16, kernel_size=5, strides=1, activation='tanh', padding='valid'))

#S4 Pooling layer
model.add(AveragePooling2D(pool_size=2, strides=2, padding='valid'))

#C5 Convolutional layer
model.add(Conv2D(filters=120, kernel_size=5, strides=1, activation='tanh', input_shape=(28,28,1), padding='valid'))

model.add(Flatten())

