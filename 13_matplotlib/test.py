import matplotlib.pyplot as plt

fig, subplot = plt.subplots()

# ��������� �������� �� Matplotlib
print("������ Figure: %s, \n������ subplot: %s, \n������������� ������ � ������� Subplot: %s\n" % (
    type(fig), type(subplot), type(fig.axes[0])
))
# ������ ������ ����� � ������ ��������� c � ������� ������ plot
subplot.plot([0], 'o', color='black')