from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from lr import lr_scheduler
from lenet5 import model

#set leraning rate schedule
lr_scheduler = LearningRateScheduler(lr_scheduler)

#set a checkpoint
checkpointer = ModelCheckpoint(filepath='model.weights.best.hdf5', verbose=1, save_best_only=True)

#train the model
hist = model.fit()
