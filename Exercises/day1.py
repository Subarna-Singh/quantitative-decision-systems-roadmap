import numpy as np
import matplotlib.pyplot as plt

def concepts()
    Measures of Central Tendency
        Mean: average of data
        Median: middle value in sorted data
        Mode: most frequent value

    Measures of Dispersion
        Variance (σ²): average squared distance from the mean
        Standard Deviation (σ): square root of variance, measures spread in original units

    | Word                       | Meaning                     | Example                                 |
    | :------------------------- | :-------------------------- | :-------------------------------------- |
    | **Outlier**                | Data point far from others  | 500 mins delivery is an outlier         |
    | **Central Tendency**       | Center of data distribution | Mean is a central tendency measure      |
    | **Dispersion**             | Data spread                 | High variance indicates more dispersion |
    | **Skewed Distribution**    | Data leaning to one side    | Salary data is right-skewed             |
    | **Standard Deviation (σ)** | Spread around mean          | Low σ → consistent values               |


def concept_exercise():
    # Delivery times (in minutes)
    times = np.array([30, 35, 35, 40, 50, 60, 500])
    print(times)

    # Mean
    mean_time = np.mean(times)
    print(f"Mean: {mean_time}")

    # Median
    median_time = np.median(times)
    print(f"Median: {median_time}")

    # Mode (using scipy)
    from scipy import stats
    mode_time = stats.mode(times, keepdims=False)
    print(f"Mode: {mode_time}")

    # Variance
    variance_time = np.var(times)
    print(f"Variance: {variance_time}")

    # # Standard Deviation
    std_dev_time = np.std(times)
    print(f"Standard Deviation: {std_dev_time}")


def visual_exercise():

    # Data
    times = np.array([30, 35, 35, 40, 50, 60, 500])

    # Mean and Std Dev
    mean_time = np.mean(times)
    std_dev_time = np.std(times)

    # Plotting
    plt.hist(times, bins=20, color='skyblue', edgecolor='black')
    plt.axvline(mean_time, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_time:.2f}')
    plt.axvline(mean_time + std_dev_time, color='green', linestyle='dotted', linewidth=2, label=f'+1σ: {mean_time + std_dev_time:.2f}')
    plt.axvline(mean_time - std_dev_time, color='green', linestyle='dotted', linewidth=2, label=f'-1σ: {mean_time - std_dev_time:.2f}')

    plt.title('Delivery Times Distribution')
    plt.xlabel('Minutes')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    concept_exercise()
    visual_exercise()