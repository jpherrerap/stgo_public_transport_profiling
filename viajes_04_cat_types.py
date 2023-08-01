import pandas as pd

comuna_types = pd.CategoricalDtype(categories=['MAIPU', 'INDEPENDENCIA', 'CONCHALI', 'RECOLETA',
                  'QUILICURA', 'HUECHURABA', 'PROVIDENCIA', 'RENCA',
                  'PUDAHUEL', 'ESTACION CENTRAL', 'LO PRADO', 'SANTIAGO',
                  'CERRO NAVIA', 'QUINTA NORMAL', 'CERRILLOS', 'NUNOA',
                  'VITACURA', 'LO BARNECHEA', 'LAS CONDES', 'LA REINA',
                  'PENALOLEN', 'SAN MIGUEL', 'SAN JOAQUIN', 'LA GRANJA',
                  'LA FLORIDA', 'LA PINTANA', 'EL BOSQUE', 'PUENTE ALTO',
                  'SAN BERNARDO', 'SAN RAMON', 'LA CISTERNA',
                  'PEDRO AGUIRRE CERDA', 'LO ESPEJO', 'MACUL'], ordered=False)

period_types = pd.CategoricalDtype(categories=['00:00:00', '00:30:00', '01:00:00', '01:30:00', '02:00:00',
                  '02:30:00', '03:00:00', '03:30:00', '04:00:00', '04:30:00',
                  '05:00:00', '05:30:00', '06:00:00', '06:30:00', '07:00:00',
                  '07:30:00', '08:00:00', '08:30:00', '09:00:00', '09:30:00',
                  '10:00:00', '10:30:00', '11:00:00', '11:30:00', '12:00:00',
                  '12:30:00', '13:00:00', '13:30:00', '14:00:00', '14:30:00',
                  '15:00:00', '15:30:00', '16:00:00', '16:30:00', '17:00:00',
                  '17:30:00', '18:00:00', '18:30:00', '19:00:00', '19:30:00',
                  '20:00:00', '20:30:00', '21:00:00', '21:30:00'], ordered=True)

medio_types = pd.CategoricalDtype(categories=['METRO', 'BUS', 'ZP', 'METROTREN'], ordered=True)

dtypes = {
    'comunasubida': comuna_types,
    'comunabajada': comuna_types,
    'mediahora': period_types,
    'tipotransporte_1era': medio_types,
    'tipotransporte_2da': medio_types,
    'tipotransporte_3era': medio_types,
    'tipotransporte_4ta': medio_types}