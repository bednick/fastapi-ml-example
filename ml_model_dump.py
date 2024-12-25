import pickle


from fastapi_ml_example.ml_models import ExampleMLModel


if __name__ == "__main__":
    with open("model.pkl", "wb") as fp:
        pickle.dump(ExampleMLModel(), fp)
