import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

ax.plot(x, y)
ax.set_title('Mon premier graphique')
ax.set_xlabel('Abscisses')
ax.set_ylabel('Ordonnées')

plt.show()
