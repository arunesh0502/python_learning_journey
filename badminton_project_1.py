import matplotlib.pyplot as plt
import numpy as np

# My 17 year career data
years = np.arange(2008,2025)
age = np.arange(7,25)

# Approximate performace level over the years (on a scale of 1-10)
performance = [4, 5, 5, 5, 6, 5, 6, 6, 7, 6, 7, 8, 9, 9, 8, 8, 6]

# Training hours every day over the years (approximate)
training_hours = [2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 7, 6, 6, 5, 5, 4]

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Subplot 1: Performance Over Time
ax1.plot(years, performance, color='black', marker='o', linewidth=2, markersize=6)
ax1.fill_between(years, performance, color='red', alpha=0.2)
ax1.set_xlabel('YEAR', fontsize=12, fontweight='bold')
ax1.set_ylabel('PERFORMANCE LEVEL', fontsize=12, fontweight='bold')
ax1.set_title('PERFORMANCE OVER TIME', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0,10)

# Annotations for Key Milestones
ax1.annotate('PEAK PERFORMANCE', xy=(2020,9), xytext=(2018,9.5),
             arrowprops=dict(color='red', arrowstyle='->'),
             fontsize=10, color='red')

#Subplot 2: Training Hours Over Career
ax2.bar(years, training_hours, color='red', alpha=1)
ax2.set_xlabel('YEAR', fontsize=12, fontweight='bold')
ax2.set_ylabel('TRAINING HOURS', fontsize=12, fontweight='bold')
ax2.set_title('TRAINING INTENSITY OVER CAREER', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

# Adding text with career statistics
total_hours=np.sum(training_hours)*200  #Excluding sundays and match days(approximate)
stats_text=f' Total Career Statistics: \n 17 Years Completed \n {total_hours:,} Hours Trained in Total\n Peak Performance Level: {np.max(performance)}/10'
ax2.text(2008, 9, stats_text, fontsize=10, bbox=dict(boxstyle='round', facecolor='coral', alpha=0.2))

plt.tight_layout()
plt.savefig('badminton_career_analysis.png', dpi=300, bbox_inches='tight')
plt.show()
print('Visualisation saved as badminton_career_analysis.png')