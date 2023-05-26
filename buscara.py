import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path  # doctest: +SKIP

def distritalxProvincia(provincias):
    for provincia in provincias:
        provincia = provincia.upper()
        df = pd.read_excel(f"central_table-{provincia}.xlsx")
        df1 = pd.read_excel("indicadores_dengue_diario_distrito.xlsx")
        df1.replace({"LA TINGUIÑA": "LA TINGUINA"})
        df1.replace("PARIÑÃ‰AS", "PARIÑAS",inplace=True)
        df1.replace('PARIÑÉAS', 'PARIÑAS', inplace=True)

        dt = datetime.now()
        str_time = dt.strftime("%d-%m-%Y")
        ##Filtrando por departamentos
        df1 = df1[df1['Departamento'] == provincia.upper()]
        dfFinal = pd.merge(df, df1, on="Distrito", how="outer")
        dfFinal = dfFinal.rename(columns={'Incidencia* x100mil': 'Incidencia*'})
        dfFinal = dfFinal.rename(columns={'Casos*': 'Personas contagiadas'})
        dfFinal = dfFinal.rename(columns={'Fallecidos*': 'Personas fallecidas'})
        dfFinal.replace(0.0, '', inplace=True)
        
        filepath = Path(f'./dengue_diario-{provincia}.csv')  # doctest: +SKIP
        filepath.parent.mkdir(parents=True, exist_ok=True)  # doctest: +SKIP
        # df.to_csv(filepath)

        dfFinal.to_csv(filepath, columns=['id','Distrito','Personas contagiadas','Incidencia*','Personas fallecidas'], index=False, encoding='utf-8')
        print(f'archivo guardado dengue_diario-{provincia}.csv')

provincias = ["Lima", "Piura", "Loreto", "Ica", "Ucayali"]

distritalxProvincia(provincias)
print("archivo finalizado")