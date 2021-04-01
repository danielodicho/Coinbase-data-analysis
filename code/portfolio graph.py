import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

x = []
y = []
palette = plt.get_cmap('Set1')
for line in open('values2.txt', 'r'):
    lines = [x for x in line.split()]
    x.append((lines[0]))
    y.append(float(lines[1]))

myValues = {'ADA': [], 'BTC': [], 'ETH': [], 'FIL': []}
time = []
for x in open('myCrypto.txt', 'r'):
    lines = [y for y in x.split()]
    myValues[lines[1]].append(float(lines[2]))
    if lines[0] not in time:
        time.append(lines[0])

print(time, myValues)

counter = 0
for x in myValues:
    counter += 1
    plt.plot(time, myValues[x],  marker='', color=palette(counter), linewidth=3, alpha=0.8, label=x)




plt.title("My Portfolio")
plt.legend(loc=2, ncol=1)
plt.xlabel("Time")
plt.ylabel("Euro")
plt.show()




