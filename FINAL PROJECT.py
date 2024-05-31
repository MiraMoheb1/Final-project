import streamlit as st
import pickle
import pandas as pd

# Streamlit application title and information
st.title('Heart Disease Prediction')
st.info('Predict the likelihood of heart disease based on several health indicators.')

# Sidebar for feature selection
st.sidebar.header('Feature Selection')

# Input fields for user to input features
Sex = st.sidebar.selectbox('Sex', ['Female', 'Male'])
GeneralHealth = st.sidebar.selectbox('General Health', ['Very good', 'Excellent', 'Fair', 'Poor', 'Good'])
LastCheckupTime = st.sidebar.selectbox('Last Checkup Time', [
    'Within past year (anytime less than 12 months ago)',
    'Within past 2 years (1 year but less than 2 years ago)',
    'Within past 5 years (2 years but less than 5 years ago)',
    '5 or more years ago'
])
PhysicalActivities = st.sidebar.selectbox('Physical Activities', ['No', 'Yes'])
RemovedTeeth = st.sidebar.selectbox('Removed Teeth', ['None of them', '6 or more, but not all', '1 to 5', 'All'])
HadHeartAttack = st.sidebar.selectbox('Had Heart Attack', ['No', 'Yes'])
HadAngina = st.sidebar.selectbox('Had Angina', ['No', 'Yes'])
HadStroke = st.sidebar.selectbox('Had Stroke', ['No', 'Yes'])
HadAsthma = st.sidebar.selectbox('Had Asthma', ['No', 'Yes'])
HadSkinCancer = st.sidebar.selectbox('Had Skin Cancer', ['No', 'Yes'])
HadCOPD = st.sidebar.selectbox('Had COPD', ['No', 'Yes'])
HadDepressiveDisorder = st.sidebar.selectbox('Had Depressive Disorder', ['No', 'Yes'])
HadKidneyDisease = st.sidebar.selectbox('Had Kidney Disease', ['No', 'Yes'])
HadArthritis = st.sidebar.selectbox('Had Arthritis', ['No', 'Yes'])
HadDiabetes = st.sidebar.selectbox('Had Diabetes', [
    'Yes', 'No', 'No, pre-diabetes or borderline diabetes',
    'Yes, but only during pregnancy (female)'
])
DeafOrHardOfHearing = st.sidebar.selectbox('Deaf or Hard of Hearing', ['No', 'Yes'])
BlindOrVisionDifficulty = st.sidebar.selectbox('Blind or Vision Difficulty', ['No', 'Yes'])
DifficultyConcentrating = st.sidebar.selectbox('Difficulty Concentrating', ['No', 'Yes'])
DifficultyWalking = st.sidebar.selectbox('Difficulty Walking', ['No', 'Yes'])
DifficultyDressingBathing = st.sidebar.selectbox('Difficulty Dressing or Bathing', ['No', 'Yes'])
DifficultyErrands = st.sidebar.selectbox('Difficulty with Errands', ['No', 'Yes'])
SmokerStatus = st.sidebar.selectbox('Smoker Status', [
    'Never smoked', 'Current smoker - now smokes some days', 'Former smoker',
    'Current smoker - now smokes every day'
])
ECigaretteUsage = st.sidebar.selectbox('E-Cigarette Usage', [
    'Not at all (right now)', 'Never used e-cigarettes in my entire life',
    'Use them every day', 'Use them some days'
])
ChestScan = st.sidebar.selectbox('Chest Scan', ['No', 'Yes'])
RaceEthnicityCategory = st.sidebar.selectbox('Race/Ethnicity Category', [
    'White only, Non-Hispanic', 'Black only, Non-Hispanic',
    'Other race only, Non-Hispanic', 'Multiracial, Non-Hispanic', 'Hispanic'
])
AgeCategory = st.sidebar.selectbox('Age Category', [
    'Age 80 or older', 'Age 55 to 59', 'Age 65 to 69', 'Age 40 to 44',
    'Age 75 to 79', 'Age 70 to 74', 'Age 60 to 64', 'Age 50 to 54',
    'Age 45 to 49', 'Age 35 to 39', 'Age 30 to 34', 'Age 25 to 29',
    'Age 18 to 24'
])
AlcoholDrinkers = st.sidebar.selectbox('Alcohol Drinkers', ['No', 'Yes'])
HIVTesting = st.sidebar.selectbox('HIV Testing', ['No', 'Yes'])
FluVaxLast12 = st.sidebar.selectbox('Flu Vaccine in Last 12 Months', ['Yes', 'No'])
PneumoVaxEver = st.sidebar.selectbox('Pneumonia Vaccine Ever', ['No', 'Yes'])
TetanusLast10Tdap = st.sidebar.selectbox('Tetanus Shot in Last 10 Years', [
    'Yes, received tetanus shot but not sure what type',
    'No, did not receive any tetanus shot in the past 10 years',
    'Yes, received Tdap', 'Yes, received tetanus shot, but not Tdap'
])
HighRiskLastYear = st.sidebar.selectbox('High Risk Last Year', ['No', 'Yes'])
CovidPos = st.sidebar.selectbox('Covid Positive', [
    'No', 'Yes',
    'Tested positive using home test without a health professional'
])

# Data selected by the user
data_selected = pd.DataFrame({
    'Sex': [Sex],
    'GeneralHealth': [GeneralHealth],
    'LastCheckupTime': [LastCheckupTime],
    'PhysicalActivities': [PhysicalActivities],
    'RemovedTeeth': [RemovedTeeth],
    'HadHeartAttack': [HadHeartAttack],
    'HadAngina': [HadAngina],
    'HadStroke': [HadStroke],
    'HadAsthma': [HadAsthma],
    'HadSkinCancer': [HadSkinCancer],
    'HadCOPD': [HadCOPD],
    'HadDepressiveDisorder': [HadDepressiveDisorder],
    'HadKidneyDisease': [HadKidneyDisease],
    'HadArthritis': [HadArthritis],
    'HadDiabetes': [HadDiabetes],
    'DeafOrHardOfHearing': [DeafOrHardOfHearing],
    'BlindOrVisionDifficulty': [BlindOrVisionDifficulty],
    'DifficultyConcentrating': [DifficultyConcentrating],
    'DifficultyWalking': [DifficultyWalking],
    'DifficultyDressingBathing': [DifficultyDressingBathing],
    'DifficultyErrands': [DifficultyErrands],
    'SmokerStatus': [SmokerStatus],
    'ECigaretteUsage': [ECigaretteUsage],
    'ChestScan': [ChestScan],
    'RaceEthnicityCategory': [RaceEthnicityCategory],
    'AgeCategory': [AgeCategory],
    'AlcoholDrinkers': [AlcoholDrinkers],
    'HIVTesting': [HIVTesting],
    'FluVaxLast12': [FluVaxLast12],
    'PneumoVaxEver': [PneumoVaxEver],
    'TetanusLast10Tdap': [TetanusLast10Tdap],
    'HighRiskLastYear': [HighRiskLastYear],
    'CovidPos': [CovidPos]
})
model=pickle.load(open(r"C:\Users\MIRA\Downloads\heart5.sav",'rb'))
# Button to confirm prediction
Con = st.sidebar.button('Confirm')
if Con:
    result = model.predict(data_selected)
    st.write('Prediction result:', 'Heart Disease' if result[0] == 1 else 'No Heart Disease')
