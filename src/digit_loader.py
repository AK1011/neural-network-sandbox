### Code to create data and load it for digital numbers ###


def load_digit_data():
   training_validation_test_inputs = [[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1], [0,1,0,1,1,0,0,1,0,0,1,0,1,1,1], [0,1,1,1,0,1,0,0,1,0,1,0,1,1,1], [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1], [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1], [1,1,1,1,0,0,1,1,0,0,0,1,1,1,0], [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1], [1,1,1,1,0,1,0,0,1,0,0,1,0,0,1], [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1], [1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]]

   training_results = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]]

   training_data = zip(training_validation_test_inputs, training_results)
   validation_test_results = [0,1,2,3,4,5,6,7,8,9]
   validation_data = zip(training_validation_test_inputs, validation_test_results)
   test_data = zip(training_validation_test_inputs, validation_test_results)
   return (training_data, validation_data, test_data)


#The idea is to see if with only a few input possibilities to learn from, it can learn more precisely for just those. If it can learn well enough for that, we can observe each of the intermediate neurons to hopefully see how they actually interact to form an opinion on the input. Basically, with very few input possibilities, we can pick a delta that should have a large enough impact at the input level and observe exactly how that affects the next level in practice on a learned system.