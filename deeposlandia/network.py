"""Define a class that represents typical convolutional neural networks
"""

import keras as K

class ConvolutionalNeuralNetwork:
    """Convolutional neural network design
    """

    def __init__(self, network_name="mapillary", image_size=512,
                 nb_channels=3, nb_labels=65, learning_rate=1e-4):
        """ Class constructor
        """
        self._network_name = network_name
        self._image_size = image_size
        self._nb_channels = nb_channels
        self._nb_labels = nb_labels
        self._X = K.layers.Input(shape=(image_size, image_size, nb_channels))

    def convolution(self, x, nb_filters, kernel_size, strides=1, padding="same",
                    activation='relu', batch_norm=True):
        """Apply a convolutional layer within a neural network

        Use Keras API

        Parameters
        ----------
        x : tensor
            Input layer
        nb_filters : integer
            Number of convolution filters
        kernel_size : integer
            Convolution filter size, in pixel
        strides : integer
            Convolution strides, in pixel
        padding : str
            Border pixel management ("valid" to apply convolution pixel only on image pixels, or
        "same" to replicate border pixels)
        activation : str
            Type of activation function to apply on the tensor at the end of the convolution block
        ('relu' by default)
        batch_norm : boolean
            If True, a batch normalization process is applied on `x` tensor before activation
            layer

        Returns
        -------
        tensor
            4D output layer
        """
        x = K.layers.Conv2D(nb_filters, kernel_size=kernel_size,
                            strides=strides, padding='same')(x)
        if batch_norm:
            x = K.layers.BatchNormalization()(x)
        x = K.layers.Activation(activation)(x)
        return x

    def transposed_convolution(self, x, nb_filters, kernel_size, strides=1,
                               padding="same", activation='relu', batch_norm=True):
        """Build a layer seen as the transpose operation of classic convolution, for a convolutional neural
        network

        Use Keras API

        Parameters
        ----------
        x : tensor
            Input tensor
        nb_filters : integer
            Number of convolution filters
        kernel_size : integer
            Convolution filter size, in pixel
        strides : integer
            Convolution strides, in pixel
        padding : str
            Border pixel management ("valid" to apply convolution pixel only on image pixels, or
        "same" to replicate border pixels)
        activation : str
            Type of activation function to apply on the tensor at the end of the convolution block
        ('relu' by default)
        batch_norm : boolean
            If True, a batch normalization process is applied on `x` tensor before activation
            layer

        Returns
        -------
        tensor
            4D output layer
        """
        x = K.layers.Conv2DTranspose(nb_filters, kernel_size=kernel_size,
                                     strides=strides, padding=padding)(x)
        if batch_norm:
            x = K.layers.BatchNormalization()(x)
        x = K.layers.Activation(activation)(x)
        return x

    def maxpool(self, x, pool_size, strides=1, padding="same"):
        """Apply a max pooling layer within a neural network

        Use Keras API

        Parameters
        ----------
        x : tensor
            Input layer
        pool_size : integer
            Pooling kernel size, in pixel
        strides : integer
            Pooling strides, in pixel ; indicates the downscaling factor
        padding : str
            Border pixel management ("valid" to apply convolution pixel only on image pixels, or
        "same" to replicate border pixels)

        Returns
        -------
        tensor
            4D output layer
        """
        return K.layers.MaxPool2D(pool_size=pool_size, strides=strides, padding=padding)(x)

    def dense(self, x, depth, dropout_rate=1.0, activation='relu', batch_norm=True):
        """Apply a fully-connected layer within a neural network

        Use Keras API

        Parameters
        ----------
        x : tensor
            Input layer
        depth : integer
            Number of neurons used within the layer
        activation : str
            Type of activation function to apply on the tensor at the end of the convolution block
        ('relu' by default)
        dropout_rate: tensor
            tensor corresponding to the neuron keeping probability during dropout operation
        batch_norm : boolean
            If True, a batch normalization process is applied on `x` tensor before activation
            layer

        Returns
        -------
        tensor
            2D output layer
        """
        x = K.layers.Flatten()(x)
        x = K.layers.Dense(depth)(x)
        if batch_norm:
            x = K.layers.BatchNormalization()(x)
        x = K.layers.Activation(activation)(x)
        x = K.layers.Dropout(dropout_rate)(x)
        return x
