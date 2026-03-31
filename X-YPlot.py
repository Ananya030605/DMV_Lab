import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

country1_temps = [25, 26, 27, 28, 25.5, 28, 29.5, 27, 27.5, 28, 30]
country2_temps = [19, 21, 22, 23, 25.5, 21, 22.5, 24, 22, 23.5, 25]
country3_temps = [20, 21.5, 22, 22.5, 24, 20.5, 23, 21.5, 22, 23.5, 20]
country4_temps = [18, 22.5, 20, 21.5, 21, 22.5, 22, 22.5, 23, 23.5, 24]

fig, ax = plt.subplots()

ax.plot(years, country1_temps, label='Country 1')
ax.plot(years, country2_temps, label='Country 2')
ax.plot(years, country3_temps, label='Country 3')
ax.plot(years, country4_temps, label='Country 4')

ax.set_xlabel('Year')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Temperature Variation over Years for Four Countries')

ax.legend()

plt.show()