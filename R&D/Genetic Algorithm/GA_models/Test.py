from fileinput import filename
import pygad
import numpy
import pygad.kerasga
import tensorflow
import numpy as np

global data_inputs, keras_ga, model

data_inputs = [[0.13, 1.0, 3.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 10.0, 500.0, 2.0, 1.0, 2.0, 7.0]]

def fitness_func(solution, sol_idx):
    global data_inputs, keras_ga, model
    model_weights_matrix = pygad.kerasga.model_weights_as_matrix(model=model, weights_vector=solution)
    model.set_weights(weights=model_weights_matrix)
    predictions = model.predict(data_inputs)
    mae = tensorflow.keras.losses.MeanAbsoluteError()
    solution_fitness = 1.0

    return solution_fitness

def callback_generation(ga_instance):
    global data_inputs, keras_ga, model
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))



input_layer  = tensorflow.keras.layers.Input(15)
dense_layer1 = tensorflow.keras.layers.Dense(5, activation="relu")(input_layer)
output_layer = tensorflow.keras.layers.Dense(1, activation="linear")(dense_layer1)
model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)
weights_vector = pygad.kerasga.model_weights_as_vector(model=model)
keras_ga = pygad.kerasga.KerasGA(model=model, num_solutions=10)


filename = "Genetic Algorithm//GA_models//Final_Dataset"
ga_instance = pygad.load(filename=filename)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model, weights_vector=solution)

model.set_weights(best_solution_weights)
predictions = model.predict(data_inputs)
print(predictions)
#ga_instance.plot_fitness(title="Generation vs. Fitness", linewidth=4)
