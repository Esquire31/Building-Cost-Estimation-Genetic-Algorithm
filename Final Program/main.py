from flask import Flask, request, render_template
from fileinput import filename
import pygad
import numpy
import pygad.kerasga
import tensorflow
import numpy as np

app = Flask(__name__)

global data_inputs, keras_ga, model

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


def predict_outcome(data_inputs):
    global keras_ga, model
    input_layer  = tensorflow.keras.layers.Input(15)
    dense_layer1 = tensorflow.keras.layers.Dense(5, activation="relu")(input_layer)
    output_layer = tensorflow.keras.layers.Dense(1, activation="linear")(dense_layer1)
    model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)
    weights_vector = pygad.kerasga.model_weights_as_vector(model=model)
    keras_ga = pygad.kerasga.KerasGA(model=model, num_solutions=10)

    filename = "Final_Dataset"
    ga_instance = pygad.load(filename=filename)
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model, weights_vector=solution)


    model.set_weights(best_solution_weights)
    predictions = model.predict(data_inputs)
    predictions = predictions[0][0]*1000000//1

    return predictions


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/calculate', methods =["GET", "POST"])
def calculate():
    global data_inputs, keras_ga, model
    if request.method == "POST":
        values = list(request.form.listvalues())
        area = np.float64(int(values[0][0])/10000)
        no_floor = np.float64(values[0][1])
        parking = np.float64(values[0][2])
        duration = np.float64(values[0][3])
        escalations = np.float64(values[0][4])
        change = np.float64(values[0][5])
        earthwork = np.float64(values[0][6])
        foundation = values[1]
        external = values[2]
        ceiling = values[3]
        internal = values[4]
        form = values[5]
        sub = values[6]
        super_structure = values[7]
        floor = values[8]

        if sub[0]=="RCC":
            sub=np.float64(1)
        
        if super_structure[0]=="RCC":
            super_structure=np.float64(1)

        if ceiling[0]=="Non_Asbestos":
            ceiling=np.float64(1)
        elif ceiling[0]=="Gypsum_Board":
            ceiling=np.float64(2)
        
        if form[0]=="Ganged":
            form=np.float64(1)
        elif form[0]=="Conventional":
            form=np.float64(2)

        if external[0]=="Oil":
            external=np.float64(1)
        elif external[0]=="Enamel":
            external=np.float64(2)
        elif external[0]=="Emulsion":
            external=np.float64(3)

        if foundation[0]=="Mat":
            foundation=np.float64(1)
        elif foundation[0]=="Wall_Footing":
            foundation=np.float64(2)
        elif foundation[0]=="Pile":
            foundation=np.float64(3)

        if internal[0]=="Acrylic":
            internal=np.float64(1)
        elif internal[0]=="Emulsion":
            internal=np.float64(2)
        elif internal[0]=="Gypsum_Board":
            internal=np.float64(3)

        if floor[0]=="Marble":
            floor=np.float64(1)
        elif floor[0]=="Vinyl":
            floor=np.float64(2)
        elif floor[0]=="Laminate":
            floor=np.float64(3)

        data_inputs = [[area,ceiling,external,internal,floor,foundation,form,super_structure,sub,change,duration,earthwork,no_floor,parking,escalations]]

        print(data_inputs)

        sum = predict_outcome(data_inputs)

        final_output = f"Predicted output based on the best solution: {sum}"
    print(final_output)
    return render_template("main.html",predict_content = final_output)


if __name__ == '__main__':
    app.run()