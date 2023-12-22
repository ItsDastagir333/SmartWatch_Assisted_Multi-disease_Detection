import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Sleep_apnea_model = pickle.load(open('sleep_apnea_model.sav', 'rb'))

AFib_model = pickle.load(open('afib_model.sav', 'rb'))

Stress_model = pickle.load(open('stress_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('SmartWatch Assisted Multiple Disease Prediction System',
                          
                          ['Sleep Apnea Prediction',
                           'AFib Prediction',
                           'Stress Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Sleep Apnea Prediction Page
if (selected == 'Sleep Apnea Prediction'):
    
    # page title
    st.title('Sleep Apnea Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        HeartRate = st.text_input('HeartRate')
        
    with col2:
        Spo2 = st.text_input('Spo2')
    
    with col3:
        Spo2Drops = st.text_input('Spo2Drops')
    
    
    
    # code for Prediction
    SA_diagnosis= ''
    
    # creating a button for Prediction
    
    if st.button('Sleep Apnea Test Result'):
        SA_Prediction = Sleep_apnea_model.predict([[HeartRate, Spo2, Spo2Drops]])
        
        if (SA_Prediction[0] == 1):
          SA_diagnosis= 'The person has Sleep Apnea'
        else:
          SA_diagnosis= 'The person does not have Sleep Apnea'
        
    st.success(SA_diagnosis)




# AFib Prediction Page
if (selected == 'AFib Prediction'):
    
    # page title
    st.title('AFib Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        HR = st.text_input('HeartRate')
        
    with col2:
        SpO2 = st.text_input('SpO2')
        
    with col3:
        Stress_Level = st.text_input('Stress Level')
        
    with col1:
        Age = st.text_input('Age')

    with col2:
        Gender = st.text_input('Gender')
        
    with col3:
        Hypertension = st.text_input('Hypertension')
        
    with col1:
        Diabetes = st.text_input('Diabetes')

    with col2:
        Heart_Disease=st.text_input('Heart Disease')
        
    with col3:
        Obesity = st.text_input('Obesity')

    with col1:
        Smoking = st.text_input('Smoking')
        
    with col2:
        Alcohol = st.text_input('Alcohol')

    with col3:
        Family_History_of_AF = st.text_input('Family History of AF')
        
    with col1:
        BMI = st.text_input('BMI')
       
     
     
    # code for Prediction
    AFib_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('AFib Test Result'):
        AFib_prediction = AFib_model.predict([[HR ,SpO2, Stress_Level, Age,	Gender,	Hypertension, Diabetes,	Heart_Disease, Obesity, Smoking, Alcohol, Family_History_of_AF, BMI]])                          
        
        if (AFib_prediction[0] == 1):
          AFib_diagnosis = 'The person is having AFib'
        else:
          AFib_diagnosis = 'The person does not have AFib'
        
    st.success(AFib_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Stress Prediction"):
    
    # page title
    st.title("Stress Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        HeartRate = st.text_input('HeartRate(bpm)')
        
    with col2:
        Spo2 = st.text_input('SpO2(%)')
        
    with col3:
        ActivityLevel = st.text_input('Activity_Level(0-1)')
        
    with col1:
        UserInput = st.text_input('Do you think you are stresssed (0-NO || 1-YES)')
        

        
    
    
    # code for Prediction
    stress_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Stress Test Result"):
        stress_prediction = Stress_model.predict([[HeartRate, SpO2, Activity_Level, User_input]])                          
        
        if (stress_prediction[0] == 1):
          stress_diagnosis = "The person is Stress"
        else:
          stress_diagnosis = "The person is not Stressed"
        
    st.success(stress_diagnosis)
