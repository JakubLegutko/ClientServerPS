
from itertools import count
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import string
import sys
while True:
       try:
        address = sys.argv[1]
        break
       except IndexError :
            print("Usage: serial_port.py filename where filename is data file that server recieved")
            sys.exit()
fo = open(address,'r')
ax1 = plt.subplot(3, 1, 1)
ax2 = plt.subplot(3, 1, 2)
ax3 = plt.subplot(3, 1, 3)

ax1.set_ylim((-1.2,1.2))
ax2.set_ylim((-1.2,1.2))
ax3.set_ylim((-1.2,1.2))

#plt.style.use('fivethirtyeight')

t_vals = []
x_vals = []
y_vals = []
z_vals = []
index = count()
def animate(i):

    KLO5Data = fo.readline()
    KLO5Data.replace(' ','')
    if KLO5Data.strip():
        
        KLO5Data.replace('\x00','')
        print(KLO5Data)
        data = KLO5Data.split(',')
        print(data)

        conv_data = []
        for element in data:
            print(element)
            conv_data.append(element.strip())
            
        print(conv_data)
        graph_data = [float(i) for i in conv_data]
        print(graph_data)
        print("GRAPH")
        t_vals.append(next(index))

        x_vals.append(graph_data[0])
        y_vals.append(graph_data[1])
        z_vals.append(graph_data[2])
        ax1.plot(t_vals,x_vals,color='r')
        ax2.plot(t_vals,y_vals,color='b')
        ax3.plot(t_vals,z_vals,color='g')
ani = FuncAnimation(plt.gcf(), animate , interval = 10)
plt.show()
