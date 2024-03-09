import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

emissions_file_path = 'emissions/GCB2022v27_MtCO2_flat.csv'
emissions_df = pd.read_csv(emissions_file_path)

belgium_emissions = emissions_df[emissions_df['ISO 3166-1 alpha-3'] == 'BEL']
switzerland_emissions = emissions_df[emissions_df['ISO 3166-1 alpha-3'] == 'CHE']

belgium_carbon_pricing = pd.read_csv('carbontax/national/wcpd_co2_Belgium.csv')
switzerland_carbon_pricing = pd.read_csv('carbontax/national/wcpd_co2_Switzerland.csv')

# co2 emissions comparison
plt.figure(figsize=(12, 6))
sns.lineplot(data=belgium_emissions, x='Year', y='Total', label='Belgium', marker='o')
sns.lineplot(data=switzerland_emissions, x='Year', y='Total', label='Switzerland', marker='o')
plt.title('Total CO2 Emissions Comparison')
plt.xlabel('Year')
plt.ylabel('Total CO2 Emissions (Million Metric Tons)')
plt.legend()
plt.show()
