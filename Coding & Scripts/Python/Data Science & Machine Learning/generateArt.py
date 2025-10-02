"""
       _____                           _   _                         _                               _       _   _   _      _                      _          _______          _   ___
      / ____|                         | | (_)               /\      | |                             (_)     | | | \ | |    | |                    | |        / / ____|   /\   | \ | \ \
     | |  __  ___ _ __   ___ _ __ __ _| |_ ___   _____     /  \   __| |_   _____ _ __ ___  __ _ _ __ _  __ _| | |  \| | ___| |___      _____  _ __| | __    | | |  __   /  \  |  \| || |
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __| \ \ / / _ \   / /\ \ / _` \ \ / / _ \ '__/ __|/ _` | '__| |/ _` | | | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /    | | | |_ | / /\ \ | . ` || |
     | |__| |  __/ | | |  __/ | | (_| | |_| |\ V /  __/  / ____ \ (_| |\ V /  __/ |  \__ \ (_| | |  | | (_| | | | |\  |  __/ |_ \ V  V / (_) | |  |   <     | | |__| |/ ____ \| |\  || |
      \_____|\___|_| |_|\___|_|  \__,_|\__|_| \_/ \___| /_/    \_\__,_| \_/ \___|_|  |___/\__,_|_|  |_|\__,_|_| |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\    | |\_____/_/    \_\_| \_|| |
                                                                                                                                                             \_\                    /_/
"""

# Import libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# Define the generator model
def make_generator_model():
    model = tf.keras.Sequential()
    model.add(layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Reshape((7, 7, 256)))
    assert model.output_shape == (None, 7, 7, 256)  # Note: None is the batch size

    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    assert model.output_shape == (None, 7, 7, 128)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    assert model.output_shape == (None, 14, 14, 64)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    assert model.output_shape == (None, 28, 28, 1)

    return model

# Create the generator
generator = make_generator_model()

# Generate a random noise vector
noise = tf.random.normal([1, 100])

# Generate an image from the noise
generated_image = generator(noise, training=False)

# Display the generated image
import matplotlib.pyplot as plt
plt.imshow(generated_image[0, :, :, 0], cmap='gray')
plt.show()
