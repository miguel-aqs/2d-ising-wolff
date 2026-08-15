# 2D Ising Model - Wolff Monte Carlo Simulation

***This is a two-part project! You can find Part I where I use a simpler (but less efficient) algorithm [here](https://github.com/miguel-aqs/2d-ising-wolff).***

This is a simple Monte Carlo Markov Chain simulation made with the intent to model magnets as a large grid of cells, each representing an atom's individual 'spin' or what can be thought of as magnetic charge.

Each atom on the grid tends toward the action of least energy. At low temperatures, the energy of neighboring spins attempting to align dominates, forcing the lattice to rapidly minimize energy and snap into giant, highly ordered ferromagnetic domains. These will, granted a large enough grid and along enough time, all eventually align to either +1 or -1. 

Raising the temperature past a certain critical temperature dissolves the magnetic structure into high-entropy, uncorrelated static flipping back and forth as thermal energy is injected, overpowering magnetic bonds.

These probabilities are governed by the Boltzmann distribution, through a Hamiltonian. This Hamiltonian takes the form of a Metropolis algorithm in the code.

In 1944, Lars Onsager solved the 2D Ising model, finding the critical temperature at which the magnet loses its ferromagnetism to be at roughly `T ≈ 2.269`.

*Note that Boltzmann's constant is set to 1 in order to avoid underflow errors, so T is measured in natural units.*

## Parameters
The parameters that can be easily adjusted in `ising.py` are:
* **Grid size** (Resolution of the atomic lattice)
* **Impurities** (Probability of each cell having a spin of 0)
* **Steps per frame** (Math steps calculated before updating the screen)
* **Temperature** (`T`)
* **Show graph** (Toggleable)
* **Show slider*** (Toggleable)

## Learn More
Read more about the physics [here](https://en.wikipedia.org/wiki/Ising_model).
Learn more about the math and the Hamiltonian [here](https://www.youtube.com/watch?v=BHHoTagq03A).
