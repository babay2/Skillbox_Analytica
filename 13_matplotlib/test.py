import matplotlib.pyplot as plt

fig, subplot = plt.subplots()

# Типизация объектов из Matplotlib
print("объект Figure: %s, \nобъект subplot: %s, \nИерархический доступ к объекту Subplot: %s\n" % (
    type(fig), type(subplot), type(fig.axes[0])
))
# рисуем жирную точку в начале координат c с помощью метода plot
subplot.plot([0], 'o', color='black')