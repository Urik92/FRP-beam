import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb
from streamlit_option_menu import option_menu


model=xgb.XGBRegressor()
model.load_model('xgb_model.json')

model_2=xgb.XGBRegressor()
model_2.load_model('xgb_model_with_stirrup.json')

# sidebar for navigate

with st.sidebar:
    selected = option_menu("multiple FRP beam shear predictive system",
                           ['FRP beam with stirrup prediction system',
                            'FRP beam without stirrup prediction system'],
                           icons =['hdd-rack-fill','hdd-stack-fill'],
                           
                           default_index = 0)
    
# FRP beam with stirrup pages
if (selected == 'FRP beam with stirrup prediction system'):
    
    # page title
    st.title('Shear prediction of FRP beam with stirrup  using ML')
    
    st.write('')
    st.write('')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        p1=st.slider(" Width of the Beam (mm)",135.000,914.000)
         
    with col2:
        p2=st.slider("Effective Depth of the Beam (mm)",170.0,937.0)
    
    with col3:
        p3=st.slider("Compressive Strength of Concrete (mpa)",20.0,84.2)
        
    with col1:
        p4=st.slider("Longitudnal FRP bar ratio (%)",0.0039,0.0398)
        
    with col2:
        p5=st.slider("Modulus of elascity of longitudnal bar (mpa)",29000.0,140000.0)
        
    with col3:
        p6=st.slider("shear FRP bar ratio (%)",0.0003,0.02) 
        
    with col1:
        p7=st.slider("spacing (mm)",24.0,406.0)
        
    with col2:
        p8=st.slider("Modulus of elascity of shear bar (mpa)",10000.0,241000.0)
        
    with col3:
        p9=st.slider("Manufacture FRP strength (mpa)",230.0,4500.0)
        
    with col1:
       p10=st.slider("Shear span to depth ratio (a/d)",1.2,4.4) 
    
    
    data_new_ws=pd.DataFrame({
    'bw':p1,
    'd':p2,
    'fc':p3,
    'longt_ratio':p4,
    'Efl':p5,
    'shear_rebar_ratio':p6,
    's':p7,
    'Efw':p8,
    'ffuw':p9,
    'a_over_d':p10    
    
},index=[0])
    
    if st.button('predict'):
        pred=model_2.predict(data_new_ws)
        st.balloons()
        st.success(" shear strength of FRP beam is {:.2f} KN".format(pred[0]))
        
    
if (selected == 'FRP beam without stirrup prediction system'):
    
    # page title
    st.title('Shear prediction of FRP beam without stirrup  using ML')
    st.write('')
    st.write('')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        p1=st.slider(" Width of the Beam (mm)",89.0,1000.0)
        
    with col2:
        p2=st.slider("Effective Depth of the Beam (mm)",73.0,1111.0)
        
    with col3:
        p3=st.slider("Compressive Strength of Concrete (mpa)",19.2,93.0) 
        
    with col1:
        p4=st.slider("Longitudnal FRP bar ratio (%)",0.0012,1.24) 
        
    with col2:
         p5=st.slider("Modulus of elascity (mpa)",29000.0,192000.0)
    
    with col3:
        p6=st.slider("Shear span to depth ratio (a/d)",1.0,12.5)
    
    
    data_new=pd.DataFrame({
    'bw':p1,
    'd':p2,
    'fc':p3,
    'longt_ratio':p4,
    'Efl':p5,
    'a_over_d':p6
},index=[0])
    
    if st.button('predict'):
        pred=model.predict(data_new)
        st.balloons()
        st.success(" shear strength of FRP beam is {:.2f} KN".format(pred[0]))
        
st.write('By: Kirubel Girma')    
st.write("Advisor: Tesfaye Alemu (Ph.D)")

    
    
    
    
    
    
    
    
    
    