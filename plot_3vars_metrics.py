import pandas as pd
import matplotlib.pyplot as plt

def plot_3vars(csv_file, metric_name, ylabel, output_file):
    df = pd.read_csv(csv_file, comment="#")
    var_names = list(df.columns)

    problem_sizes = df[var_names[0]].values.tolist()
    code1 = df[var_names[1]].values.tolist()
    code2 = df[var_names[2]].values.tolist()
    code3 = df[var_names[3]].values.tolist()

    plt.figure()
    plt.title(f"{metric_name} vs. Problem Size")
    xlocs = [i for i in range(len(problem_sizes))]
    plt.xticks(xlocs, problem_sizes, rotation=45)
    plt.plot(code1, "r-o", label="Direct Sum")
    plt.plot(code2, "b-x", label="Vector Sum")
    plt.plot(code3, "g-^", label="Indirect Sum")
    plt.xlabel("Problem Size (N)")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

# Plot MFLOP/s
plot_3vars(
    "mflops.csv",
    "MFLOP/s",
    "Performance (MFLOP/s)",
    "mflops_vs_problem_size.png"
)

# Plot % Memory Bandwidth Utilized
plot_3vars(
    "memory_bandwidths.csv",
    "Memory Bandwidth Utilization",
    "Memory Bandwidth Utilization (% of Peak)",
    "memory_bandwidth_vs_problem_size.png"
)

# Plot Memory Latency
plot_3vars(
    "memory_latencys.csv",
    "Memory Latency",
    "Memory Latency (ns)",
    "memory_latency_vs_problem_size.png"
)