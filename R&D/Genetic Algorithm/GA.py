import tensorflow.keras
import pygad.kerasga
import numpy
import numpy as np
import pygad
import csv

def fitness_func(solution, sol_idx):
    global data_inputs, data_outputs, keras_ga, model
    model_weights_matrix = pygad.kerasga.model_weights_as_matrix(model=model, weights_vector=solution)
    model.set_weights(weights=model_weights_matrix)
    predictions = model.predict(data_inputs)
    mae = tensorflow.keras.losses.MeanAbsoluteError()
    abs_error = mae(data_outputs, predictions).numpy() + 0.00000001
    solution_fitness = 1.0 / abs_error

    return solution_fitness


def callback_generation(ga_instance):
    global data_inputs, data_outputs, keras_ga, model
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))



input_layer  = tensorflow.keras.layers.Input(15)
dense_layer1 = tensorflow.keras.layers.Dense(5, activation="relu")(input_layer)
output_layer = tensorflow.keras.layers.Dense(1, activation="linear")(dense_layer1)
model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)
weights_vector = pygad.kerasga.model_weights_as_vector(model=model)
keras_ga = pygad.kerasga.KerasGA(model=model, num_solutions=10)


def genetic_algorithm_train(filename):
    rows=[]
    inputs=[]
    outputs=[]
    global data_inputs, data_outputs, keras_ga, model
    with open(f"Genetic Algorithm//{filename}.csv", 'r') as f:
        dataset = csv.reader(f)
        header = next(dataset)
        for row in dataset:
            rows.append(row)
    f.close()
    for i in range(0,len(rows)):
        area = np.float64(rows[i][0])
        ceiling = np.float64(rows[i][1])
        external = np.float64(rows[i][2])
        internal = np.float64(rows[i][3])
        floor = np.float64(rows[i][4])
        foundation = np.float64(rows[i][5])
        form = np.float64(rows[i][6])
        super = np.float64(rows[i][7])
        sub = np.float64(rows[i][8])
        changes = np.float64(rows[i][9])
        duration = np.float64(rows[i][10])
        earthwork = np.float64(rows[i][11])
        floors = np.float64(rows[i][12])
        parking = np.float64(rows[i][13])
        escalation = np.float64(rows[i][14])
        cost = np.float64(rows[i][15])
        inputs.append([area,ceiling,external,internal,floor,foundation,form,super,sub,changes,duration,earthwork,floors,parking,escalation])
        outputs.append([cost])

    data_inputs = np.array(inputs)
    data_outputs = np.array(outputs)

    num_generations = 500
    num_parents_mating = 3
    initial_population = keras_ga.population_weights
    ga_instance = pygad.GA(num_generations=num_generations, num_parents_mating=num_parents_mating, initial_population=initial_population, fitness_func=fitness_func, on_generation=callback_generation, stop_criteria=["reach_0.1", "saturate_15"])
    ga_instance.run()

    #ga_instance.plot_result(title="PyGAD & Keras - Iteration vs. Fitness", linewidth=4)

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

    best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model, weights_vector=solution)

    model.set_weights(best_solution_weights)
    predictions = model.predict(data_inputs)
    print("Predictions : \n", predictions)

    mae = tensorflow.keras.losses.MeanAbsoluteError()
    abs_error = mae(data_outputs, predictions).numpy()
    print("Absolute Error : ", abs_error)
    saving = input("Do you want to save the model based on predictions? [Y/n]: ")
    if saving.lower()=="y":
        ga_instance.save(f"Genetic Algorithm//GA_models//{filename}")
    else:
        genetic_algorithm_train(filename=filename)

genetic_algorithm_train("Final_Dataset")