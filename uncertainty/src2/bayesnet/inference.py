from model import model

# Calculate predictions
predictions = model.predict_proba({
#    "rain": "heavy",
    "train": "delayed"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print("{}: {}".format(node.name,prediction))
    else:
        print("{}".format(node.name))
        for value, probability in prediction.parameters[0].items():
            print("    {}: {}".format(value,probability))
