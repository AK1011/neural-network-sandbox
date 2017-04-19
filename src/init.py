import network
import mnist_loader
import digit_loader

def init_minst(neurons=30, epochs=30, mini_batch_size=10, eta=3.0):
   training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
   net = network.Network([784, neurons, 10])
   net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)

def init_digit(neurons=4, epochs=10, mini_batch_size=1, eta=3.0):
   training_data, validation_data, test_data = digit_loader.load_digit_data()
   net = network.Network([15, neurons, 10])
   net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)