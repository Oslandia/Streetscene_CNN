
"""Design a feature detection model with Keras API
"""

import keras as K

from deeposlandia.network import ConvolutionalNeuralNetwork

class FeatureDetectionNetwork(ConvolutionalNeuralNetwork):
    """
    """

    def __init__(self, network_name="mapillary", image_size=512, nb_channels=3,
                 nb_labels=65, learning_rate=1e-4, architecture="simple"):
        ConvolutionalNeuralNetwork.__init__(self, network_name, image_size,
                                            nb_channels, nb_labels, learning_rate)
        if architecture == "vgg16":
            self.Y = self.vgg16()
        elif architecture == "vgg19":
            self.Y = self.vgg19()
        elif architecture == "inception-v1":
            self.Y = self.inception_v1()
        elif architecture == "inception-v2":
            self.Y = self.inception_v2()
        elif architecture == "inception-v3":
            self.Y = self.inception_v3()
        elif architecture == "inception-v4":
            self.Y = self.inception_v4()
        elif architecture == "Xception":
            self.Y = self.xception()
        elif architecture == "resnet":
            self.Y = self.resnet()
        else:
            self.Y = self.simple()

    def output_layer(self, x, depth):
        """Build an output layer to a neural network, as a dense layer with sigmoid activation
        function as the point is to detect multiple labels on a single image

        Parameters
        ----------
        x : tensor
            Previous layer within the neural network (last hidden layer)
        depth : integer
            Dimension of the previous neural network layer

        Returns
        -------
        tensor
            2D output layer
        """
        y = K.layers.Dense(depth, name='output_fc')(x)
        y = K.layers.Activation(activation='sigmoid', name='output_activation')(y)
        return y

    def simple(self):
        """Build a simple default convolutional neural network composed of 3 convolution-maxpool
        blocks and 1 fully-connected layer

        Returns
        -------
        tensor
            Output predictions, that have to be compared with ground-truth values
        """
        layer = self.convolution(self.X, nb_filters=16, kernel_size=7, name='conv1')
        layer = self.maxpool(layer, pool_size=2, strides=2, name='pool1')
        layer = self.convolution(layer, nb_filters=32, kernel_size=5, name='conv2')
        layer = self.maxpool(layer, pool_size=2, strides=2, name='pool2')
        layer = self.convolution(layer, nb_filters=64, kernel_size=3, name='conv3')
        layer = self.maxpool(layer, pool_size=2, strides=2, name='pool3')
        layer = self.flatten(layer, name='flatten1')
        layer = self.dense(layer, depth=512, dropout_rate=0.75, name='fc1')
        return self.output_layer(layer, depth=self._nb_labels)

    def vgg16(self):
        """
        """
        pass

    def vgg19(self):
        """
        """
        pass

    def inception_v1(self):
        """
        """
        pass
    
    def inception_v2(self):
        """
        """
        pass

    def inception_v3(self):
        """
        """
        pass

    def inception_v4(self):
        """
        """
        pass

    def xception(self):
        """
        """
        pass

    def resnet(self):
        """
        """
        pass