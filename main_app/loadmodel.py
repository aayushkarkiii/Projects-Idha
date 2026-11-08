import joblib as jb
loaded_model = jb.load('trained_model')
print(type(loaded_model))