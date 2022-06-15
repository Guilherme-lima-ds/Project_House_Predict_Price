import streamlit as st
import pickle
import pandas as pd
from flask import Flask
st.set_page_config(layout='wide')
#--------------------------Read Model-----------------------
model = pickle.load(open('model/Random_Forest_Regressor_hp.pkl','rb'))
best_worst_scenario = pd.read_csv('datasets/Melhor_Pior_Cenario.csv')
#Inicinado tudo do zero, fazendo de uma forma mais profissional agora.

#Titulo
st.title('Previsão dos Preço do Imóvel')

#Subtitulo
st.markdown('Esse WebApp Foi criado no intuito de resolver o problema na hora de precificar o preço de algum imóvel \
    graças a ele podemos ter uma clara visão se estamos fazendo um bom negócio ou não.')


#Selecionando os atributos
st.subheader('Faturamento da empresa no melhor e pior cenário')
#...

st.sidebar.subheader('Defina os atributos do imóvel para predição do valor mais adequado')


#-----------------------------------NUMBER INPUT----------------------------
OverallQual = st.sidebar.number_input('OverallQual',step=1,min_value=0,max_value=10,value=0)
GrLivArea = st.sidebar.number_input('GrLivArea',step=500.00,min_value=500.00,max_value=5700.00,value=520.00)
GarageArea = st.sidebar.number_input('GarageArea',step=150.00,min_value=150.00,max_value=1500.00,value=186.00)
_1stFlrSF = st.sidebar.number_input('1stFlrSF',step=400.00,min_value=300.00,max_value=4500.00,value=386.00)
TotalBsmtSF = st.sidebar.number_input('TotalBsmtSF',step=100.00,min_value=105.00,max_value=6110.00,value=405.00)
BsmtFinSF1 = st.sidebar.number_input('BsmtFinSF1',step=100.00,min_value=0.00,max_value=5600.00,value=464.00)
FullBath = st.sidebar.number_input('FullBath',step=1,min_value=1,max_value=7)
YearBuilt = st.sidebar.number_input('YearBuilt',min_value=1880,max_value=2010)
LotFrontage = st.sidebar.number_input('LotFrontage',step=20.00,min_value=30.00,max_value=315.00)
LotArea = st.sidebar.number_input('LotArea',step=500.00,min_value=1300.00,max_value=215245.00,value=10706.00)
OverallCond = st.sidebar.number_input('OverallCond',step=1,min_value=0,max_value=10,value=0)

#-------------------------------SELECT BOX---------------------------------
aux = {'ExterQual': 0}
ExterQual = st.sidebar.selectbox('ExterQual',['Fa','TA','Gd','Ex'])
if ExterQual == 'Fa':
    aux['ExterQual'] = 1
elif ExterQual == 'TA':
    aux['ExterQual'] = 2
elif ExterQual == 'Gd':
    aux['ExterQual'] = 3
else:
    aux['ExterQual'] = 4



aux1 = {'BsmtQual':0}
BsmtQual = st.sidebar.selectbox('BsmtQual',['Fa','TA','Gd','Ex'])
if ExterQual == 'Fa':
    aux1['BsmtQual'] = 1
elif ExterQual == 'TA':
    aux1['BsmtQual'] = 2
elif ExterQual == 'Gd':
    aux1['BsmtQual'] = 3
else:
    aux1['BsmtQual'] = 4

#----------------------------Dicionario--------------------------------
aux_dict = {'OverallQual':OverallQual,'GrLivArea':GrLivArea,'GarageArea':GarageArea,'1stFlrSF':_1stFlrSF,
           'TotalBsmtSF':TotalBsmtSF,'BsmtFinSF1':BsmtFinSF1,'FullBath':FullBath,'YearBuilt':YearBuilt,
            'LotFrontage':LotFrontage,'LotArea':LotArea,'OverallCond':OverallCond}
aux_dict.update(aux)
aux_dict.update(aux1)
dataframe = pd.DataFrame(aux_dict,index=[0])


#------------------------Melhor e Pior Cenário--------------------------

cenario = st.write(best_worst_scenario)

#-------------------------------Predict---------------------------------

botao = st.button('Prever Valor do Imóvel')
if botao:
    preco = model.predict(dataframe)
    st.write('O preço previsto para esse imóvel é: ')
    result = 'R$ '+ str(round(preco[0]*10,2))
    st.write(result)