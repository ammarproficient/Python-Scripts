import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Loading the dataset
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to the range [0, 1]
# x_train, x_test = x_train / 255.0, x_test / 255.0


#  I choose softmax activation function
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28, 28)),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])

# here I choose adam optimizer
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# Train the model
# model.fit(x_train, y_train, epochs=3)

# Save the model where you want to save and you can name your model
# model.save("handwritten_model.h5")

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# the below code is used for predict the character

# the below code is used for loading the model to predict the character
model = tf.keras.models.load_model("handwritten_character_recognition_model.h5")

# the below code can print the loss and accuracy of the trained model
# loss, accuracy = model.evaluate(x_test, y_test)
# print(loss, "\n", accuracy)

try:
    img = cv2.imread("1.png", cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))

    img = np.invert(img)
    img = img / 255.0

    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img)
    print(f"The digit is probably {np.argmax(prediction)}")

    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()
except Exception as e:
    print("Error:", e)
