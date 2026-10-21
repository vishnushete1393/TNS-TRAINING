# app.py -- a small Streamlit web app that loads our saved pipeline and makes live predictions.
# Run it from a terminal (not from this notebook) with:  streamlit run app.py

# streamlit: the library that turns this script into a web app
import streamlit as st

# pandas: to build a one-row table from the user's input, the same shape our pipeline expects
import pandas as pd

# joblib: to load the pipeline we saved from the notebook
import joblib

# load our saved pipeline once when the app starts
model = joblib.load("student_pass_predictor.joblib")

# a title shown at the top of the web page
st.title("Will This Student Pass?")

# a plain line of instructional text, shown just below the title
st.write("Enter a student's details below, and the model will predict pass or fail.")

# st.slider(label, minimum, maximum, default) -- creates a draggable slider on the page
# and returns whatever number the user has it set to, every time the page updates
hours_studied = st.slider("Hours studied", 0.0, 10.0, 5.0)
attendance_pct = st.slider("Attendance percent", 0.0, 100.0, 75.0)
previous_score = st.slider("Previous test score", 0.0, 100.0, 65.0)

# st.selectbox(label, options) -- creates a dropdown menu, and returns whichever option is chosen
study_method = st.selectbox("Study method", ["Group", "Solo", "Online"])

# a button -- the code below only runs when the user clicks it
if st.button("Predict"):

    # build a one-row DataFrame with the exact same column names the pipeline was trained on
    input_row = pd.DataFrame([{
        "hours_studied": hours_studied,
        "attendance_pct": attendance_pct,
        "previous_score": previous_score,
        "study_method": study_method
    }])

    # the pipeline cleans (impute/scale/encode) AND predicts, in one call
    prediction = model.predict(input_row)[0]

    # predict_proba gives us the model's confidence, not just its final answer
    probability = model.predict_proba(input_row)[0][1]

    # show a big, clear result on the page
    if prediction == 1:
        # st.success shows a green box -- used here for a PASS prediction
        st.success(f"Prediction: PASS (confidence: {probability:.0%})")
    else:
        # st.error shows a red box -- used here for a FAIL prediction (not a code error!)
        st.error(f"Prediction: FAIL (confidence: {1 - probability:.0%})")
