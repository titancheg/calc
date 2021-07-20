import pandas as pd
import streamlit as st

x = st.sidebar.selectbox('Выберите что будем считать:', ['Введение', 'Замес гранулы','Пленку','Пакеты','Бахилы','Перчатки', 'Заказ на бахилы'])

if x == 'Введение':
    st.write('')
    st.write('')
    st.title('Введение')
    st.subheader('Для работы калькулятора выберите в боковом меню нужный расчёт !')
    st.markdown('*Для входа в боковое меню на устройстве с маленьким экраном нажмите, в левом вверхнем углу, значок в виде стрелки  ">"*')
    st.write('')
    st.header('Контакты:')
    st.markdown('**Телефон для связи: ** [8-903-260-96-61](tel:+79032609661)')
    st.markdown('**Адрес: ** [Московская область, город Серпухов, улица Коншиных, 113А](https://yandex.ru/mApS/10754/serpuhov/house/ulitsa_konshinykh_113a/Z04YdQ9iSkwEQFtufXVzcXVqbA==/?ll=37.382394%2C54.920998&z=17)')
    st.markdown('**Почта: ** [8007005448@mail.ru](mailto:8007005448@mail.ru)')
    st.markdown('**Корпоративный сайт: ** [tpkpromed.ru](https://tpkpromed.ru)')
    st.markdown('**Производство бахил: ** [bioinvn.ru](https://bioinvn.ru)')
    st.markdown('**Интернет магазин: ** [pmpsale.ru](https://pmpsale.ru)')
    
if x == 'Замес гранулы':
   
elif x == "Пленку":
    
elif x == "Пакеты":
    

elif x == "Бахилы":
    
    
elif x == "Перчатки":
    
elif x == "Заказ на бахилы":
   
