from matplotlib.figure import Figure

bins = ["A", "B", "C", "D", "E", "F"]
values = [3,  5,  8,  4,  2,  1]
cumul  = [3,  8, 16, 20, 22, 23]

fig = Figure()
ax1, ax2 = fig.subplots(2, 1)
fig.suptitle("Répartition par appréciation")
ax1.bar(bins, values)
ax2.bar(bins, cumul)
