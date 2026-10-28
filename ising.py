import numpy as np
import random
import matplotlib.pyplot as plt
import csv
import multiprocessing as mp


"""---CONFIG STUFF---"""

initial_state = 0 # 0 = completely random, 1 = all +1 spin, -1 = all -1 (no in between)

"""------------------"""

def init_lattice(N, pct_impurity):
    if initial_state == 0:
        p_spin = (1 - pct_impurity) / 2
        spins = np.random.choice([0, -1, 1], size=(N, N), p=[pct_impurity, p_spin, p_spin])
    elif initial_state == 1:
        p_spin = 1 - pct_impurity
        spins = np.random.choice([0, -1, 1], size=(N, N), p=[pct_impurity, 0, p_spin])
    elif initial_state == -1:
        p_spin = 1 - pct_impurity
        spins = np.random.choice([0, -1, 1], size=(N, N), p=[pct_impurity, p_spin, 0])
    return spins



def wolff(spins, N, T, J=1.0):
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)

    if spins[i, j] == 0:
        return

    seed = spins[i, j]

    prob = np.exp((-2 * J) / T)
    P_add = 1 - prob

    cluster = set([(i, j)])

    stack = [(i, j)]

    while stack:
        current_i, current_j = stack.pop()

        neighbors = [
            ((current_i + 1) % N, current_j),
            ((current_i - 1) % N, current_j),
            (current_i, (current_j + 1) % N),
            (current_i, (current_j - 1) % N)
        ]

        for ni, nj in neighbors:
            if spins[ni, nj] == seed:
                if (ni, nj) not in cluster:
                    if random.random() < P_add:
                        cluster.add((ni, nj))
                        stack.append((ni, nj))

    for oi, oj in cluster:
        spins[oi, oj] *= -1
        
    

def get_abs_magnetization(spins):
    active_spins = spins[spins != 0]
    return abs(np.mean(active_spins)) if len(active_spins) != 0 else 0.0



def find_Tc(N, pct_impurity):
    print(f"Calculating Tc for {pct_impurity*100:.2f}% impurities... (this may take a minute)")
    
    G = init_lattice(N, pct_impurity)
    
    temperatures = np.linspace(2.5, 0.05, 100)
    susceptibilities = []


    n_thermal = int(500 * (N / 50))
    n_measure = int(1000 * (N / 50))

    for T in temperatures:
        for _ in range(n_thermal):
            wolff(G, N, T)
        measurements = []
        for _ in range(n_measure):
            wolff(G, N, T)
            measurements.append(get_abs_magnetization(G))

        chi = np.var(measurements) / T
        susceptibilities.append(chi)

    print(f"Finished {pct_impurity*100:.2f}%!")
    return temperatures[np.argmax(susceptibilities)]

if __name__ == "__main__":
    N = 250
    impurities = np.linspace(0, 0.45, 20)

    impurity_data = list(impurities)

    tasks = [(N, I) for I in impurities]

    print(f"Starting simulation across {mp.cpu_count()} CPU cores")

    with mp.Pool() as pool:
        Tc_data = pool.starmap(find_Tc, tasks)

    print("Saving data to csv")
    with open("simulation_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Impurity Percentage", "Curie Temperature"])
        for x, y in zip(impurity_data, Tc_data):
            writer.writerow([x, y])
    print("Simulation complete! File saved as simulation_results.csv")
