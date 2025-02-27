import google.generativeai as genai

genai.configure(api_key="AIzaSyDyJNQAMUw6t_pbBdoka2Q_u0qFWiIaAQw")

models = genai.list_models()
for model in models:
    print(model.name)
