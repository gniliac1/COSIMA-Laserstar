# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:01:36 2018

@author: Cailing
"""
# Give a summary about the model
model.summary()

# Delete the model
del model

# Automaticly save weights as "checkpoints" while training
checkpoint_path = "../data/training_1/cp-{epoch:04d}.ckpt"
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, verbose=1, save_weights_only=True,
    # Save weights, every 2-epochs.
    period=2)
model.fit(train_images, train_labels, epochs=10,callbacks=[cp_callback])

# Save weights on your own
model.save_weights('./checkpoints/my_checkpoint')

# Load weights
model.load_weights('./checkpoints/my_checkpoint')

# Save entire model to a HDF5-File (some whired standard)
model.save('my_model.h5')

# Load model including optimizer and weights
new_model = keras.models.load_model('my_model.h5')
