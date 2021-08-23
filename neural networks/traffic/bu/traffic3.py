import cv2
import numpy as np
import os
import sys
import tensorflow as tf

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
            
            image=image/255.0
            images.append(cv2.resize(image,(IMG_WIDTH,IMG_HEIGHT),3))			
#            images.append(cv2.resize(image,(IMG_WIDTH,IMG_HEIGHT),3))
            labels.append(i)

    #print(images[0])
    return(images,labels)
        
        
    
    
    #raise NotImplementedError


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    act0='elu'
    act1='relu'
    model = tf.keras.models.Sequential([

    # Convolutional layer. Learn 32 filters using a 3x3 kernel
    tf.keras.layers.Conv2D(
        140, (3, 3), activation=act1, input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    ),


    # Max-pooling layer, using 2x2 pool size

    #tf.keras.layers.MaxPooling2D(pool_size=(3, 2)),


    tf.keras.layers.Conv2D(
        30,(2, 2), activation=act0),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(
        10,(3, 3), activation=act0),
    tf.keras.layers.Conv2D(
        42,(4, 3), activation=act0),





  #  tf.keras.layers.Conv2D(
   #     13, (2, 2), activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),


 #   tf.keras.layers.Conv2D(
 #       10,(3, 3), activation=act0),
   # tf.keras.layers.Dropout(0.2),






    # Flatten units
    tf.keras.layers.Flatten(),

    # Add a hidden layer with dropout
    tf.keras.layers.Dense(200, activation=act1),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(140, activation=act0),
    tf.keras.layers.Dense(132, activation=act1),

    tf.keras.layers.Dense(320, activation=act1),

    tf.keras.layers.Dense(116, activation=act0),

  #  tf.keras.layers.Dense(117, activation=act1),
    tf.keras.layers.Dense(50, activation=act0),
  #  tf.keras.layers.Dense(100, activation=act1),
  #  tf.keras.layers.Dropout(0.3),


    tf.keras.layers.BatchNormalization(
    axis=-1,
    momentum=0.95979,
    epsilon=0.00531,
    center=True,
    scale=True,
    beta_initializer="zeros",
    gamma_initializer="ones",
    moving_mean_initializer="zeros",
    moving_variance_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
    renorm=False,
    renorm_clipping=None,
    renorm_momentum=0.9019,
    fused=None,
    trainable=True,
    virtual_batch_size=None,
    adjustment=None,
    name=None),

    # Add an output layer with output units for all NUM_CATEGORIES digits
    tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
])

    
    opt=tf.keras.optimizers.RMSprop(
    learning_rate=0.0107,
    rho=0.9,
    momentum=1e-9,
    epsilon=1e-06,
    centered=False
)
    opt = tf.keras.optimizers.Adam(learning_rate=0.0073)

    
    #opt=tf.keras.optimizers.Adamax(
    #learning_rate=0.09, beta_1=0.9, beta_2=0.999, epsilon=1e-07, name="Adamax") 

    #loss_fn=tf.keras.losses.KLDivergence(reduction="auto", name="kl_divergence")
    #loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
    loss_fn="categorical_crossentropy"
    #loss_fn=tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")
    # Train neural network
    model.summary()
    model.compile(
    optimizer=opt,#RMSprop(),#"adam",
    loss=loss_fn,#"categorical_crossentropy",
    metrics=["accuracy"]
    )
    return model
    
    #raise NotImplementedError


if __name__ == "__main__":
    main()
