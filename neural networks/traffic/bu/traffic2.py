import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print("Model saved to {}.".format(filename))


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    
    images=[]; labels=[]
    for i in range(NUM_CATEGORIES):
    
        for img in os.listdir(os.path.join(data_dir,str(i))):
            #print(os.path.join(data_dir,str(i),img))
            image=cv2.imread(os.path.join(data_dir,str(i),img))
            images.append(np.resize(image,(IMG_WIDTH,IMG_HEIGHT,3)))
            
            labels.append(i)
    print(images)
    return((images,labels))
        
        
    
    
    raise NotImplementedError


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    
#     model = tf.keras.models.Sequential([

#     # Convolutional layer. Learn 32 filters using a 3x3 kernel
#     tf.keras.layers.Conv2D(
#         16, (2, 2), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
#     ),


#     # Max-pooling layer, using 2x2 pool size

#   #  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),


#     tf.keras.layers.Conv2D(
#         7,(2, 3), activation="relu"),
#     tf.keras.layers.Conv2D(
#         7,(4, 4), activation="relu"),
#     tf.keras.layers.Conv2D(
#         7,(2, 3), activation="relu"),





#     tf.keras.layers.Conv2D(
#         13, (3, 2), activation="relu"),
#     # # Max-pooling layer, using 2x2 pool size
#    # tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

# #    tf.keras.layers.Conv2D(
# #        13, (3,3), activation="relu"),
#     # Max-pooling layer, using 2x2 pool size
# #    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),


# #  tf.keras.layers.Conv2D(
#  #        20, (2,2), activation="relu"),
#     # # Max-pooling layer, using 2x2 pool size
#     #tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

# #    tf.keras.layers.Conv2D(
# #         5, (2, 1), activation="relu"),
#     # #Max-pooling layer, using 2x2 pool size
# #    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

#     # # Max-pooling layer, using 2x2 pool size
#     # tf.keras.layers.MaxPooling2D(pool_size=(1, 1)),


#   #  tf.keras.layers.Conv2D(
#    #      50, (2, 2), activation="relu"),
#     # # Max-pooling layer, using 2x2 pool size
#     #tf.keras.layers.MaxPooling2D(pool_size=(3, 3)),

#     #tf.keras.layers.Conv2D(
#     #     3, (2, 2), activation="relu"),
#    # tf.keras.layers.Conv2D(
#    #      10, (2, 2), activation="relu"),
#    # tf.keras.layers.Conv2D(
#    #      30, (2, 2), activation="relu"),
#   #  tf.keras.layers.Conv2D(
#   #       10, (2, 2), activation="relu"),
#     # # Max-pooling layer, using 2x2 pool size
#     # tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

#     # # Max-pooling layer, using 2x2 pool size
#     # tf.keras.layers.MaxPooling2D(pool_size=(1, 1)),


#  #   tf.keras.layers.Conv2D(
#  #        4, (2, 2), activation="relu"),
#     # # Max-pooling layer, using 2x2 pool size
# #    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

# #    tf.keras.layers.Conv2D(
# #        5, (2, 2), activation="relu"),

#  #   tf.keras.layers.Conv2D(
#  #        5, (2, 1), activation="relu"),
# #    tf.keras.layers.Conv2D(
# #         3, (1, 1), activation="relu"),

#     #tf.keras.layers.Conv2D(
#     #     5, (1, 1), activation="relu"),
#     # # Max-pooling layer, using 2x2 pool size
#     tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
#    # tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),




#     # Flatten units
#     tf.keras.layers.Flatten(),

#     # Add a hidden layer with dropout
#     tf.keras.layers.Dense(32, activation="relu"),
#     tf.keras.layers.Dropout(0.3),
#     tf.keras.layers.Dense(32, activation="relu"),
#     tf.keras.layers.Dense(32, activation="relu"),
#     tf.keras.layers.Dropout(0.6),
#     #tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(32, activation="relu"),
# #    tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(10, activation="relu"),
#     tf.keras.layers.Dense(10, activation="relu"),
#     tf.keras.layers.Dense(13, activation="relu"),
#     tf.keras.layers.Dense(104, activation="relu"),
#     tf.keras.layers.Dropout(0.2),
#     tf.keras.layers.Dense(15, activation="relu"),
#     tf.keras.layers.Dense(16, activation="relu"),
# #    tf.keras.layers.Dropout(0.3),
#     tf.keras.layers.Dense(17, activation="relu"),
#     tf.keras.layers.Dense(32, activation="relu"),
#     tf.keras.layers.Dense(130, activation="relu"),
#     tf.keras.layers.Dropout(0.1),


# #     tf.keras.layers.Dense(500, activation="relu"),
# # #    tf.keras.layers.Dense(700, activation="relu"),
# # #    tf.keras.layers.Dropout(0.5),
# #     tf.keras.layers.Dense(100, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# # #    tf.keras.layers.Dense(700, activation="relu"),
# # #    tf.keras.layers.Dropout(0.5),
# #     tf.keras.layers.Dense(100, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# # #    tf.keras.layers.Dense(700, activation="relu"),
# # #    tf.keras.layers.Dropout(0.5),
# #     tf.keras.layers.Dense(100, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# # #    tf.keras.layers.Dense(700, activation="relu"),
# # #    tf.keras.layers.Dropout(0.5),
# #     tf.keras.layers.Dense(100, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),
# #     tf.keras.layers.Dense(500, activation="selu"),
# # #    tf.keras.layers.Dense(700, activation="selu"),
# # #    tf.keras.layers.Dropout(0.5),
# #     tf.keras.layers.Dense(100, activation="relu"),
# #     tf.keras.layers.Dropout(0.3),


#     # Add an output layer with output units for all NUM_CATEGORIES digits
#     tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
# ])

    model = keras.Sequential()
    model.add(keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)))  # 250x250 RGB images
    model.add(layers.Conv2D(32, (2, 2), strides=2, activation="elu"))
    model.add(layers.Conv2D(32, (2,2), activation="elu"))
    model.add(layers.MaxPooling2D((2,2)))




    model.add(layers.Conv2D(32, (2, 2), activation="selu"))
    model.add(layers.Conv2D(32, (2, 2), activation="selu"))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(32, (2, 2), activation="elu"))
    model.add(layers.Conv2D(32, (2, 2), activation="elu"))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Dense(32, activation='elu'),)
    model.add(layers.Dense(32, activation='elu'),)
    model.add(layers.Dense(32, activation='elu'),)
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(43)),
    
    # Train neural network
    model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
    )
    return model
    
    #raise NotImplementedError


if __name__ == "__main__":
    main()
