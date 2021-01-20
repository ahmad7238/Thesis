import time
import pandas as pd
t0 = time.time()

from aquacrop.classes import *
from aquacrop.core import *

t1 = time.time()
print('importing time = ', (t1 - t0) / 60)

weather_data = prepare_weather(get_filepath('/home/ahmad/PhD/aquacropos/Input/Weather.txt'))
sandy_loam = SoilClass(soilType='SandyLoam')
wheat = CropClass('Wheat', PlantingDate='10/01')
InitWC = InitWCClass(value=['FC'])
model = AquaCropModel(SimStartTime=f'{1982}/10/01', SimEndTime=f'{1986}/05/30', wdf=weather_data,
                      Soil=sandy_loam, Crop=wheat, InitWC=InitWC)

model.initialize()
model.step(241)
df = model.Outputs
df0 = pd.DataFrame(df.Growth)
df1 = pd.DataFrame(df.Flux)
df2 = pd.DataFrame(df.Final)
df3 = pd.DataFrame(df.Water)
print('output= ', df)

input()
