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
    st.write('')
    st.write('')
    st.title('Считаем замес гранулы: ')
    az = st.number_input('Вес ввода ПНД: ')
    bz = st.number_input('Вес ввода ПНД втор.: ')
    cz = st.number_input('Вес ввода мела: ')
    dz = st.number_input('Вес ввода красителя: ')
    ez = az + bz + cz + dz
    if ez == 0:
        ez = 1
    else:
        ez < 0
    fz = az / ez
    gz = bz / ez
    hz = cz / ez
    iz = dz / ez
    st.write('В одном килограмме замеса: ')
    st.write('ПНД = ' + str(fz) + ' кг.')
    st.write('ПНД втор. = ' + str(gz) + ' кг.')
    st.write('Мел = ' + str(hz) + ' кг.')
    st.write('Краситель = ' + str(iz) + ' кг.')
    
    st.title('Себес. замеса гранулы: ')
    az1 = st.number_input('Цена ПНД: ')
    bz1 = st.number_input('Цена ПНД вторичка: ')
    cz1 = st.number_input('Цена Мела: ')
    dz1 = st.number_input('Цену Красителя: ')        
    az2 = az1 * fz
    bz2 = bz1 * gz
    cz2 = cz1 * hz
    dz2 = dz1 * iz
    xz = az2 + bz2 + cz2 + dz2    
        
    ez = st.number_input('Зарплатa сотрудников: ')
    fz = st.number_input('Стоимость аренды: ')
    gz = st.number_input('Стоимость электричества: ')
    hz = st.number_input('Стоимость кредита: ')        
    zz = ez + fz + gz + hz        
                 
    iz = st.number_input('Стоимость ТО: ')
    iz = xz * iz / 100    
                
    kz = st.number_input('Возврат за экструдер: ')
    kz = xz * kz / 100    
                
    lz = st.number_input('Введите БРАК: ')
    lz =   xz * lz / 100    
        
    yz = xz + zz + iz + kz + lz      
    st.write('Себестоимость замеса гранулы: ' + str(yz) + ' руб.')

elif x == "Пленку":
    st.write('')
    st.write('')
    st.title('Цена 1 кг. плёнки: ')
    ap = st.number_input('Длина изделия в метрах: ')
    bp = st.number_input('Ширина излелия в метрах: ')
    cp = st.number_input('Толщина в микронах: ')
    dp = st.number_input('Количество стенок: ')
    ip = int (1)
    fp = int (1000)
    gp = cp / 1000
    xp = ap * bp * gp * dp * ip * fp
    st.write('Цена 1 килограмма плёнки: ' + str(xp) + ' руб.')

elif x == "Пакеты":
    st.write('')
    st.write('')
    st.title('Цена 1 кг. пакетов: ')
    apa = st.number_input('Длина изделия: ')
    bpa = st.number_input('Ширина излелия: ')
    cpa = st.number_input('Толщина в микронах: ')
    dpa = st.number_input('Количество стенок: ')
    ipa = int (1)
    fpa = int (1000)
    gpa = cpa /1000
    xpa = apa * bpa * cpa * dpa * ipa * fpa        
    st.write('Цена 1 кг пакетов: ' + str(xpa) + ' руб.')

elif x == "Бахилы":
    st.write('')
    st.write('')
    st.title('Цена 1 кг. плёнки: ')
    ab1 = st.number_input('Вес ввода ПНД: ')
    ab2 = st.number_input('Цена ПНД: ')
    bb1 = st.number_input('Вес ввода ПНД вторичка: ')
    bb2 = st.number_input('Цена ПНД вторичка: ')
    cb1 = st.number_input('Вес ввода Мела: ')
    cb2 = st.number_input('Цена Мела: ')
    db1 = st.number_input('Вес ввода Красителя: ')
    db2 = st.number_input('Цена Красителя: ')        
    ab = ab2 * ab1
    bb = bb2 * bb1
    cb = cb2 * cb1
    db = db2 * db1
    xb = ab + bb + cb + db        
                
    eb = st.number_input('Зарплата сотрудников: ')
    fb = st.number_input('Стоимость аренды: ')
    gb = st.number_input('Стоимость электричества: ')
    hb = st.number_input('Стоимость кредита: ')        
    zb = eb + fb + gb + hb
                    
    ib = st.number_input('Стоимость ТО: ')
    ib = xb * ib / 100
                
    kb = st.number_input('Возврат за экструдер: ')
    kb = xb * kb / 100
                
    lb = st.number_input('Введите БРАК: ')
    lb =  xb * lb / 100
    yb = xb + zb + ib + kb + lb      
    st.write('Цена 1 килограмма плёнки для бахил: ' + str(yb) + ' руб.')

    st.title('Вес одной пары бахил: ')
    ab3 = st.number_input('Высота изделия в метрах: ')
    bb3 = st.number_input('Длина излелия в метрах: ')
    cb3 = st.number_input('Толщина в микронах: ')
    db3 = int (2)
    ib3 = int (1)
    gb3 = cb3 / 1000
    fb3 = int (1000)
    zb3 = ab3 * bb3 * gb3 * db3 * ib3 * fb3       
    st.write('Вес одной пары бахил: ' + str(zb3) + ' гр.')

    st.title('Себестоимость бахил: ')
    mb4 = zb3 * yb
    pb4 = mb4 * 1 /100
    ab4 = st.number_input('Зaрплата сотрудников: ')
    bb4 = st.number_input('Стоимость Аренды: ')
    cb4 = st.number_input('Стоимость Электричества: ')
    db4 = st.number_input('Стоимость Возврата электричества: ')
    eb4 = st.number_input('Стоимость TO: ')
    fb4 = st.number_input('Стоимость Скотча: ')
    gb4 = st.number_input('Стоимость Пакетов: ')
    hb4 = st.number_input('Стоимость Доставки: ')
    ib4 = st.number_input('Стоимость Кредита: ')
    jb41 = st.number_input('Стоимость Коробки: ')
    jb4 = jb41 * 1 / 100
    ob41 = pb4 + ab4 + bb4 + cb4 + db4 + eb4 + fb4 + gb4 + hb4 + ib4 + jb4

    kb41 = st.number_input('Стоимость Резинки: ')
    kb4 = kb41 * 1 / 100

    lb4 = st.number_input('Количество резинок [1 или 2]: ')
    if lb4 == '1':
        tb4 = float (kb4 * 1)            

    elif lb4 == '2':
        tb4 = float (kb4 * 2)            

    ob4 = kb4 * lb4
    zb4 = ob41 + ob4
    st.write('Себестоимость бахил: ' + str(zb4) + ' руб.')
    
elif x == "Перчатки":
    st.write('')
    st.write('')
    st.title('Цена 1 кг. плёнки: ')
    ape1 = st.number_input('Вес ввода ПНД: ')
    ape2 = st.number_input('Цена ПНД: ')
    bpe1 = st.number_input('Вес ввода ПНД вторичка: ')
    bpe2 = st.number_input('Цена ПНД вторичка: ')
    cpe1 = st.number_input('Вес ввода Мела: ')
    cpe2 = st.number_input('Цена Мела: ')
    dpe1 = st.number_input('Вес ввода Красителя: ')
    dpe2 = st.number_input('Цена Красителя: ')
    ape = ape2 * ape1
    bpe = bpe2 * bpe1
    cpe = cpe2 * cpe1
    dpe = dpe2 * dpe1
    xpe = ape + bpe + cpe + dpe
        
    epe = st.number_input('Зарплата сотрудников: ')
    fpe = st.number_input('Стоимость аренды: ')
    gpe = st.number_input('Стоимость электричества: ')
    hpe = st.number_input('Стоимость кредита: ')        
    wpe = epe + fpe + gpe + hpe
                     
    ipe = st.number_input('Стоимость ТО: ')
    ipe = xpe * ipe / 100
                
    kpe = st.number_input('Возврат за экструдер: ')
    kpe = xpe * kpe / 100
                
    lpe = st.number_input('Введите БРАК: ')
    lpe =   xpe * lpe / 100

    ype = xpe + wpe + ipe + kpe + lpe        
    st.write('Цена 1 килограмма плёнки для перчаток: ' + str(ype) + ' руб.')
        
    st.title('Вес одной пары перчаток: ')
    ape3 = st.number_input('Высота изделия в метрах: ')
    bpe3 = st.number_input('Длина излелия в метрах: ')
    cpe3 = st.number_input('Толщина в микронах: ')
    dpe3 = int (2)
    ipe3 = int (1)
    gpe3 = cpe3 / 1000
    fpe3 = int (1000)
    zpe3 = ape3 * bpe3 * gpe3 * dpe3 * ipe3 * fpe3        
    st.write('Вес одной пары перчаток: ' + str(zpe3) + ' кг.')

    st.title('Себестоимость перчаток: ')
    mpe4 = zpe3 * ype
    ppe4 = mpe4 * 1 /100
    ape4 = st.number_input('Зарплатa сотрудников: ')
    bpe4 = st.number_input('Стоимость Аренды: ')
    cpe4 = st.number_input('Стоимость Электричества: ')
    dpe4 = st.number_input('Стоимость Возврата электричества: ')
    epe4 = st.number_input('Стоимость ТO: ')
    fpe4 = st.number_input('Стоимость Скотча: ')
    gpe4 = st.number_input('Стоимость Пакетов: ')
    hpe4 = st.number_input('Стоимость Доставки: ')
    ipe4 = st.number_input('Стоимость Кредита: ')
    jpe41 = st.number_input('Стоимость Коробки: ')
    jpe4 = jpe41 * 1 / 100
    ope4 = ppe4 + ape4 + bpe4 + cpe4 + dpe4 + epe4 + fpe4 + gpe4 + hpe4 + ipe4 + jpe4        
    st.write('Себестоимость перчаток: ' + str(ope4) + ' руб.')

elif x == "Заказ на бахилы":
    st.write('')
    st.write('')
    st.title('Расчёт выполнения заказа: ')
    aza = st.number_input('Введите кол-во задейственного оборудования: ')
    if aza == 5:
            aza = 5
    elif aza == 4:
            aza = 4
    elif aza == 3:
            aza = 3
    elif aza == 2:
            aza = 2
    elif aza == 1:
            aza = 1
    elif aza == 0:
        aza = 1
    else:
        aza < 0
    
    bza = st.number_input('Выберите позицию: [Эконом = 1, Стандарт = 2, Прочные = 3, Детские = 4]')
    if bza == 1:
            bza = 40000
    elif bza == 2:
            bza = 35000
    elif bza == 3:
            bza = 30000
    elif bza == 4:
            bza = 10000
    elif bza == 0:
        bza = 1
    else:
        bza < 0
    lza = aza * bza

    cza = st.number_input('Введите график: [где 12 часов = 1, а 24 часа = 2]: ')
    if cza == 1:
            cza = 1
    elif cza == 2:
            cza = 2
    elif cza == 0:
        cza = 1
    else:
        cza < 0
    kza = lza * cza

    dza = st.number_input('Введите кол-во бахил в парах: ')
    if dza == 0:
        dza = 1
    else:
        dza < 0
    sza = dza / kza
    st.write('Для выполнения заказа нужно: ' + str(sza) + ' день/дня/дней')
