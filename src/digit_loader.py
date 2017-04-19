### Code to create data and load it for digital numbers ###


def load_digit_data():
   training_validation_test_inputs = [[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1], [0,1,0,1,1,0,0,1,0,0,1,0,1,1,1], [0,1,1,1,0,1,0,0,1,0,1,0,1,1,1], [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1], [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1], [1,1,1,1,0,0,1,1,0,0,0,1,1,1,0], [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1], [1,1,1,1,0,1,0,0,1,0,0,1,0,0,1], [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1], [1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]]

   training_results = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]]

   training_data = zip(training_validation_test_inputs, training_results)
   validation_test_results = [0,1,2,3,4,5,6,7,8,9]
   validation_data = zip(training_validation_test_inputs, validation_test_results)
   test_data = zip(training_validation_test_inputs, validation_test_results)
   return (training_data, validation_data, test_data)