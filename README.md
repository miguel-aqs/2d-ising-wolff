# 2D Ising Model - Wolff Monte Carlo Simulation

> First of all, it's technically pronounced "EE-zing" not "EYE-zing" but no one seems to care.

***This is a two-part project! You can find Part I where I use a simpler (but less efficient) algorithm [here](https://github.com/miguel-aqs/2d-ising-wolff).***


This is a simple Monte Carlo Markov Chain simulation made with the intent to model magnets as a large grid of cells, each representing an atom's individual 'spin' or what can be thought of as magnetic charge.

Each atom on the grid tends toward the action of least energy. At low temperatures, the energy of neighboring spins attempting to align dominates, forcing the lattice to rapidly minimize energy and snap into giant, highly ordered ferromagnetic domains. These will, granted a large enough grid and along enough time, all eventually align to either +1 or -1. 

Raising the temperature past a certain critical temperature dissolves the magnetic structure into high-entropy, uncorrelated static flipping back and forth as thermal energy is injected, overpowering magnetic bonds.

These probabilities are governed by the Boltzmann distribution, through a Hamiltonian. This Hamiltonian is ran through a Wolff algorithm in the code.

In 1944, Lars Onsager solved the 2D Ising model, finding the critical temperature at which the magnet loses its ferromagnetism to be at roughly `T ≈ 2.269`.

*Note that Boltzmann's constant is set to 1 in order to avoid underflow errors, so T is measured in natural units.*

## Parameters
The parameters that can be easily adjusted in `ising.py` are:
* **Grid size** (Resolution of the atomic lattice)
* **Impurities** (Probability of each cell having a spin of 0)
* **Steps per frame** (Math steps calculated before updating the screen)
* **Temperature** (`T`)
* **Show graph** (Toggleable)
* **Show slider** (Toggleable)

## Recommended Settings
Note that this was made on a laptop, so has that level of hardware in mind.

The Wolff algorithm is unbelieveably faster than the Metropolis. To be honest, I have no clue on the limits of this thing, but a successful phase transition was detected using these:

* `250x250` grid
* `5` steps per frame
* `0.39` percentage impurities
* `2.269 T` (the critical temperature of the pure Ising model)
* Initialize with random configuration.
* Drag the `T` slider slowly until around 0.7-0.9 where fractals should form: the phase transition!

## Dependencies
This project is built using standard Python and requires the following external libraries:
* **NumPy** - For efficient multidimensional grid manipulation and math.
* **Matplotlib** - For handling the live, real-time GUI animation.

## Changelog

### [August 16, 2026]
* Implemented the Wolff algorithm.
* Successfully simulated phase transition in 0.39% impurities.

### [August 15, 2026]
* Cloned the Metropolis (Part I) repo to prepare to switch the algorithms.
* Sorted through git backend bureaucracy.

## Credits

* Credit to [@Revimime](https://github.com/Revimime) for helping research Wolff vs. Swedsen-Wang algorithms.
* Credit to [@Mulletgoneviral](https://github.com/MulletGoneViral) for the git bureaucracy help.

## Learn More
Read more about the physics [here](https://en.wikipedia.org/wiki/Ising_model).
Learn more about the math and the Hamiltonian [here](https://www.youtube.com/watch?v=BHHoTagq03A).
