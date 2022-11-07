def describe_car(model, car= " Ford"):
    msg = car.title() + " type " + model.title() + "."
    print(msg)
describe_car("F-150")
describe_car("Expedition")
describe_car("Veneno", "Lamborghini")

def model_make(model, make):
    return(model.title() + "," + make.title())

model = model_make("F-150" , "Ford")
print(model)

model = model_make("Expedition" , "Ford")
print(model)

model = model_make("Veneno", "Lamborghini")
print(model)