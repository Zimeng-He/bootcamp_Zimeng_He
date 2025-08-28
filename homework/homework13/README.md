# Stage13 Productization Homework

## Project Overview
This project demonstrates the productization of a simple machine learning workflow.  
Key steps include:
- Building a mock regression model using synthetic data.
- Saving and reloading the model (model/model.pkl) for reproducibility.
- Exposing model predictions through a Flask API (/predict, /plot).
- Testing the API from a Jupyter notebook and saving evidence in reports/.

This setup simulates the handoff process of a data project:  
clean folder structure, modularized code, documentation, and working API.

---

##  Project Structure
data/ # input data (mock or real)
model/ # persisted model (model.pkl)
reports/ # plots, API test evidence
src/ # reusable functions (project.py etc.)
notebooks/ # cleaned final notebooks
app.py # Flask API
requirements.txt
README.md