import pandas as pd
import matplotlib.pyplot as plt

df_ingresados = pd.read_excel(
    r'./data/datos-asistenciales.xlsx', index_col=0, skiprows=2, sheet_name='01')
df_uci = pd.read_excel(r'./data/datos-asistenciales.xlsx',
                       index_col=0, skiprows=2, sheet_name='04')
print(df_ingresados)
df_ingresados.plot(y=['Ingresados en Planta'])
plt.show()


df_uci.plot(y=['Ingresados UCI'])
plt.show()
df = pd.merge(left=df_ingresados, right=df_uci,
              left_index=True, right_index=True)
print(df)
df.plot(y=['Ingresados en Planta', 'Ingresados UCI'])
plt.show()

df['percentage'] = (df['01 Araba_x']+df['02 Cruces_x']+df['03 Donosti_x']+df['04 Basurto_x'] +
                    df['05 Galdakao_x']+df['06 Zumarraga_x']+df['07 Bidasoa_x']+df['08 Mendaro_x'])/df['Ingresados en Planta']
df.plot(y=['percentage'])
plt.show()


df = (df - df.min()) / (df.max() - df.min())


df.plot(y=['Ingresados en Planta', 'Ingresados UCI', 'percentage'])

df.plot(y=['Ingresados en Planta',  '01 Araba_x', '02 Cruces_x',
        '03 Donosti_x', '04 Basurto_x', '05 Galdakao_x', '06 Zumarraga_x', '07 Bidasoa_x', '08 Mendaro_x'])
plt.show()


df_nor = (df - df.min()) / (df.max() - df.min())

df_nor.plot(y=['Ingresados en Planta',  '01 Araba_x', '02 Cruces_x',
               '03 Donosti_x', '04 Basurto_x', '05 Galdakao_x', '06 Zumarraga_x', '07 Bidasoa_x', '08 Mendaro_x'])
plt.show()
