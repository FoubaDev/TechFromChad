"""
Challenge DataTour 2024 : Prévision de la production d’énergie solaire en Afrique

"""
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

@st.cache_resource
def load_model():
   loaded_model = joblib.load(open('linear_model.sav', 'rb'))
   return loaded_model


@st.cache_resource
def make_predictions(input_data, _model):
    predictions = model.predict(input_data)
    input_data['Predictions'] = predictions
    input_data['id'] = input_data.index + 1
    return input_data[['id', 'country', 'Predictions']]
    
   
    
# Upload CSV file
st.title("Energie Prediction System")
st.write("Challenge DataTour 2024 : Prévision de la production d’énergie solaire en Afrique.")
uploaded_file = st.file_uploader("Upload your Submission CSV file", type=["csv"])

# create column for dashbaord
@st.cache_resource()
def dashboard():
    # Footer
    st.sidebar.markdown('---')
    
model = load_model()

def main():

    with st.sidebar:
        selected = option_menu ("Energy Prediction System",
                            
                            ['Home',
                          
                            'Author',
                            ],
                            icons = ['house','bi bi-file-medical-fill','person','book','person'],
                            default_index=0
    
                            )
    
    if(selected == "Home") :
        dashboard()
     
    if uploaded_file is not None:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(data)
        
        # Perform predictions
        if st.button("Prediction"):
            try:
                predictions = make_predictions(data, model)
                
                st.write("Predictions:")
                st.dataframe(predictions)
                
                # Option to download the updated file
                csv = data.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download predictions as CSV",
                    data=csv,
                    file_name='submission_with_predictions.csv',
                    mime='text/csv',
                )
            except Exception as e:
                st.error(f"Error making predictions: {e}")
            
    if(selected == "Author") :
        st.subheader("Author : TechFromChad")
        st.write("1. HASSANE MOUSTAPHA(https://www.linkedin.com/in/hmoustaphaousmane)")
        st.write("2. LAGRE GABBA BERTRAND(https://www.linkedin.com/in/lagrebertrand)")
        st.write("3. TEMADANG SERAPHIN(https://www.linkedin.com/in/seraphin-temadang)")
        st.write(" It is a pleasure for us to see you reading our work.")
    
    
       
        
if __name__=='__main__':
    main()
