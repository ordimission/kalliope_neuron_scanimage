import logging
import sane
from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException
from PIL import Image


logging.basicConfig()
logger = logging.getLogger("kalliope")


class Scanimage(NeuronModule):
    def __init__(self, **kwargs):

        super(Scanimage, self).__init__(**kwargs)

        self.message = None

        # get parameters form the neuron
        self.image_path = kwargs.get('image', None)
        self.mode = kwargs.get('mode', 'color')
        self.depth = kwargs.get('depth', 16)

        if self._is_parameters_ok():
            result = "";

            #
            # Initialize sane
            #
            ver = sane.init()
            print('SANE version:', ver)

            #
            # Get devices
            #
            devices = sane.get_devices()
            print('Available devices:', devices)

            #
            # Open first device
            #
            dev = sane.open(devices[0][0])

            #
            # Set some options
            #
            params = dev.get_parameters()
            try:
                dev.depth = self.depth
            except:
                logger.info('Cannot set depth, defaulting to %d' % params[3])

            try:
                dev.mode = self.mode
            except:
                logger.info('Cannot set mode, defaulting to %s' % params[0])

            #try:
            #    dev.br_x = 320.
            #    dev.br_y = 240.
            #except:
            #   print('Cannot set scan area, using default')

            params = dev.get_parameters()
            print('Device parameters:', params)

            #
            # Start a scan and get and PIL.Image object
            #
            dev.start()
            im = dev.snap()
            im.save(self.image)


            #
            # Close the device
            #
            dev.close()
            self.message = {
                "result": result
            }

            logger.info("Scanimage returned message: %s" % str(self.message))


    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: InvalidParameterException
        """

        if self.image is None:
            raise InvalidParameterException("Scanimage needs an image path")

        return True


