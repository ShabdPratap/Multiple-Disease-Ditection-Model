import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')
# loading the saved models

diabetes_model=pickle.load(open(r'C:\Users\Deepanshu mehra\Desktop\Data science\AI-ML project\diabetes_model.sav','rb'))

heart_model=pickle.load(open(r'C:\Users\Deepanshu mehra\Desktop\Data science\AI-ML project\heart_disease_model.sav','rb'))

parkinson_model=pickle.load(open(r'C:\Users\Deepanshu mehra\Desktop\Data science\AI-ML project\parkinsons_model.sav','rb'))

breast_model=pickle.load(open(r'C:\Users\Deepanshu mehra\Desktop\Data science\AI-ML project\breast_cancer.sav','rb'))

model=tf.keras.models.load_model(r'C:\Users\Deepanshu mehra\Desktop\Data science\AI-ML project\Brain_tumor_prediction_model.h5','rb')
# Sidebar for navigate

with st.sidebar:
    selected=option_menu('Multiple Disease Detection System',
        ['Diabetes Prediction','Heart Disease Prediction','Parkinson Prediction','Breast Cancer Prediction','Brain Tumor Detection'],
        icons=['activity','heart','person','plus-lg','person-hearts'],
        default_index=0)
    

# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'): 
    # Page title
    st.title('Diabetes Prediction Using ML ')

    # getting the input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')  
        
    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)      
       
if (selected == 'Heart Disease Prediction'): 
    # Page title
    st.title('Diabetes Prediction Using ML ') 
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
  
    
# Parkinson's Prediction Page
if selected == "Parkinson Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP(Fo)(Hz)')

    with col2:
        fhi = st.text_input('MDVP(Fhi)(Hz)')

    with col3:
        flo = st.text_input('MDVP(Flo)(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP(jitter)(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP(Jitter)(Abs)')

    with col3:
        RAP = st.text_input('MDVP(RAP)')

    with col1:
        PPQ = st.text_input('MDVP(PPQ)')

    with col2:
        DDP = st.text_input('Jitter(DDP)')

    with col3:
        Shimmer = st.text_input('MDVP(Shimmer)')

    with col1:
        Shimmer_dB = st.text_input('MDVP(Shimmer)(dB)')

    with col2:
        APQ3 = st.text_input('Shimmer(APQ3)')

    with col3:
        APQ5 = st.text_input('Shimmer(APQ5)')

    with col1:
        APQ = st.text_input('MDVP(APQ)')

    with col2:
        DDA = st.text_input('Shimmer(DDA)')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
if selected =='Breast Cancer Prediction' :
    # page title
    st.title("Breast Cancer Prediction using ML")

    col1, col2, col3 = st.columns(3)
    with col1:
        Radius_mean=st.text_input('radius_mean')
    with col2:
        Texture_mean=st.text_input('texture_mean') 
    with col3:
        Perimeter_mean=st.text_input('perimeter_mean')
    with col1:
        Area_mean=st.text_input('area_mean')
    with col2:
        Smoothness_mean=st.text_input('smoothness_mean')
    with col3:
        Compactness_mean=st.text_input('compactness_mean')
    with col1:
        Concavity_mean =st.text_input('concavity_mean')
    with col2:
        Concave_points_mean=st.text_input('concave_points_mean')
    with col3:
        Symmetry_mean=st.text_input('symmetry_mean')
    with col1:
        Fractal_dimension_mean=st.text_input('fractal_dimension_mean')
    with col2:
        Radius_se=st.text_input('radius_se') 
    with col3:
        Texture_se=st.text_input('texture_se')
    with col1:
        Perimeter_se=st.text_input('perimter_se')
    with col2:
        Area_se=st.text_input('area_se')
    with col3:
        Smoothness_se=st.text_input('smoothness_se')
    with col1:
        Compactness_se=st.text_input('compactness_se')
    with col2:
        Concavity_se=st.text_input('concavity_se')
    with col3:
        Concave_points_se=st.text_input('concave points_se')
    with col1:
        Symmetry_se=st.text_input('symmetry_se') 
    with col2:
        Fractal_dimension_se= st.text_input('fractal dimension_se')
    with col3:
        Radius_worst=st.text_input('radius_worst') 
    with col1:
        Texture_worst=st.text_input('texture_worst')
    with col2:
        Perimeter_worst=st.text_input('perimeter_worst')
    with col3:
        Area_worst=st.text_input('area_worst')
    with col1:
        Smoothness_worst=st.text_input('smoothness_worst')
    with col2:
        Compactness_worst=st.text_input('compactness_worst')
    with col3:
        Concavity_worst=st.text_input('concavity_worst')
    with col1:
        Concave_points_worst=st.text_input('concave_points_worst')
    with col2:
        Symmetry_worst=st.text_input('symmetry_worst')
    with col3:
        Fractal_dimension_worst=st.text_input('fractal_dimension_worst')                                  
                
    # code for Prediction
    breast_cancer_diagnosis = '' 
    
    if st.button("Breast Cancer Prediction Test Result"):

        user_input = [Radius_mean,Texture_mean,Perimeter_mean,Area_mean,Smoothness_mean,Compactness_mean,Concavity_mean,Concave_points_mean,Symmetry_mean,Fractal_dimension_mean,Radius_se,Texture_se,Perimeter_se,Area_se,Smoothness_se,Compactness_se,Concavity_se,Concave_points_se,Symmetry_se,Fractal_dimension_se,Radius_worst,Texture_worst,Perimeter_worst,Area_worst,Smoothness_worst,Compactness_worst,Concavity_worst,Concave_points_worst,Symmetry_worst,Fractal_dimension_worst]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = "The person has Parkinson's disease"
        else:
            breast_cancer_diagnosis = "The person does not have Parkinson's disease"

    st.success(breast_cancer_diagnosis)
    
if selected =='Brain Tumor Detection':
    st.title("Brain Tumor MRI Classifier\n\n")
    st.text("Upload a brain MRI Image for image classification as tumor or Healthy Brain")
        
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("Classifying...")
        
        st.write("")
        image = image.resize((224, 224))
        image_array=np.expand_dims(np.array(image)/255.0,axis=0)
        predictions=model.predict(image_array)
        
        predict_class=np.argmax(predictions)
        print("Predicted class :",predict_class);
        if predict_class==2:
            st.write("The MRI scan show a healthy brain") 
             
        else :
            st.write("The MRI scan detect a brain tumor") 