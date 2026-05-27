# Matplotlib basics
import matplotlib.pyplot as plt
import numpy as np
# Line plot
scores = [21,19,18,21,24,26,20,18,25,22]
games = [1,2,3,4,5,6,7,8,9,10]
plt.plot(games,scores,color='red')
plt.ylabel('Scores')
plt.xlabel('Games')
plt.title('Games vs Scores')
plt.show()

# Bar plot
wins = [5, 4, 8, 10, 6, 2]
opponents = ['Mauri', 'Rithu', 'Sid', 'Mano', 'Sabree', 'Arun']
plt.bar(opponents, wins, color='red')
plt.xlabel('Opponents')
plt.ylabel('Wins')
plt.title('Wins vs Opponents')
plt.show()

# Scatter plot
hours=[4,6,5,3,7,6]
performance=[20,21,25,19,24,22]
plt.scatter(hours, performance, color='red')
plt.xlabel('Hours')
plt.ylabel('Performance')
plt.title('Performance vs Hours')
plt.show()

# Editing plots
matches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [21, 18, 15, 19, 22, 17, 21, 20, 23, 19]

plt.figure(figsize=(10,6))
plt.plot(matches, scores,
         color='red',
         marker='o',
         linewidth=2,
         markersize=10,
         label='Scores',
         linestyle='-')
plt.xlabel('Matches')
plt.ylabel('Scores')
plt.title('Scores vs Matches')
plt.legend()
plt.grid('True',alpha=0.2)
plt.savefig('scores_plot.png', dpi=300, bbox_inches='tight')
plt.show()