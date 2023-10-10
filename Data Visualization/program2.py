import numpy as np
import matplotlib.pyplot as plt
T = np.array([5.6,5.8,7.9,10.5,13.7,16.8,19.1,18.7,15.9,12.3,8.4,5.9],dtype=float)
N = np.array([0,1,2,3,4,5,6,7,8,9,10,11],dtype=int)
M = np.array(['Jan','Feb','Mar','April','May','June','July','Aug','Sep','Oct','Nov','Dec'],dtype=str)
plt.title('Average Monthly Temperatures in London')
plt.xticks(N,M)
plt.ylabel('Temperature(C)')
plt.bar(N,T,width=0.8,color='#{:02x}{:02x}{:02x}'.format(120,110,160))
for i in range(0,12):
    plt.text(i-0.2,T[i]-1.2,str(T[i]))
plt.show()
