import matplotlib.pylab as plt
import numpy as np

plt.figure(figsize = (10,5))
lebdata = np.genfromtxt('life-expectancy-china-1960-2016.txt',delimiter=',',names=['x','y'])
hdidata = np.genfromtxt('hdi-china-1870-2015.txt',delimiter=',',names = ['x','y'])

plt.plot(hdidata['x'],hdidata['y'],label = 'Human Development Index')
plt.tick_params(axis='x',rotation = 70)
plt.title('China: 1870-2015')

plt.plot(lebdata['x'],lebdata['y']*0.005,label = 'Life Expectancy from Birth')
plt.plot(secondary_y = True)
plt.legend()
plt.show()