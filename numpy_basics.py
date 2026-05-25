# List basics
scores = [21,24,41,12,43,63]
opponents = ['Arun','Rithvik','Mauri','Sid','Manoj','Sabaree']
desc_scores = sorted(scores,reverse=True)
print(scores)
print(desc_scores)
print(min(scores))
print(max(scores))
print(sum(scores))
scores.count(21)
scores.index(43)
avg_score=sum(scores)/len(scores)
print(round(avg_score,2))
best_match_index=scores.index(max(scores))
best_opponent=opponents[best_match_index]
print(f'Best Score: {max(scores)}')
print(f'Best Opponent: {best_opponent}')
for i in range(len(scores)):
  if scores[i]>=avg_score:
    print(f'Match {i+1}: {scores[i]} vs {opponents[i]}')

# Numpy basics
# Numpy arrays
import numpy as np
scores = np.arange(0,100,5)
score=np.linspace(0,10000,20)
print(scores)
print(' '.join([f'{x:.0f}' for x in score]))

# Statistical functions
list=[723,283,643,512,344,983,876,326]
print('Mean: ', np.mean(list))
print('Median: ', np.median(list))
std=np.std(list)
print(f'Standard Deviation: {std:.2f}')
print('Minimum: ', np.min(list))
print('Maximum: ', np.max(list))
print('Cumulative Sum: ', np.cumsum(list))