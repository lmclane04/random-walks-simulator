# Random Walks

Mathematician Shizuo Kakutani once said "A drunk man will always find his way home, but a drunk bird will not." 
In this project, we'll investigate this claim, which is a metaphor about random walks in 2 and 3 dimensions. 

A random walk describes a sequence of steps in which each step is taken in a random direction.  
This project examines three types of random walks:

- **1D Walk**: The walker moves left or right with equal probability.  
- **2D Walk**: The walker moves up, down, left, or right with equal probability.  
- **3D Walk**: The walker moves up, down, left, right, forward, or backward with equal probability.  

A key question is whether the walker ever returns to the origin. A walk is called **recurrent** if the walker is guaranteed to return to the origin after some number of steps. It is called **transient** if there is a nonzero probability that the walker will never return to the origin. 

In Kakutani's metaphor, the **drunk man** represents a 1D or 2D random walker, while the **drunk bird** represents a 3D random walker. Using both probability theory and simulations, we explore the likelihood of returning to the origin.

---

## Simulating Random Walks
We simulate random walks in Python by generating `n` steps for `m` random walkers, tracking positions, and recording returns to the origin (see randomwalks.py)

## Simulation Results

We ran **100,000 random walks** of length **1000** in each dimension.

### Results Table

| Dimension | Avg. # of Returns | Probability of Returning at Least Once |
|-----------|------------------|----------------------------------------|
| **1D**    | 24.291           | 0.975                                  |
| **2D**    | 2.0574           | 0.6798                                 |
| **3D**    | 0.3768           | 0.2733                                 |

![Distribution of Number of Returns to Origin](distribution.png)

For 1D walks, we see a high frequency of returns to the origin, with many walks returning multiple times. For 2D walks, the frequency of returns to the origin decreases compared to 1D. For 3D Walks, returns to the origin are very rare, with most walks returning zero or very few times.

---

## Mathematical Proof (1D Random Walk)

Let \( X_i \) be a random variable for the \( i \)-th step.

- **Position after n steps**:  
  \[
  S_n = \sum_{i=1}^n X_i = N_+ - N_-
  \]  
  where \( N_+ \) = number of right steps, \( N_- \) = number of left steps.  
  Since \( N_+ + N_- = n \):  
  \[
  S_n = 2N_+ - n
  \]

- **Distribution of steps**:  
  \( N_+ \sim \text{Binomial}(n, 0.5) \).  
  \[
  E[N_+] = \frac{n}{2}, \quad Var(N_+) = \frac{n}{4}
  \]  
  Therefore,  
  \[
  E[S_n] = 0, \quad Var(S_n) = n
  \]

- **Central Limit Theorem**:  
  As \( n \to \infty \),  
  \[
  S_n \sim \mathcal{N}(0, n)
  \]

- **Probability of being at the origin after n steps**:  
  \[
  P_n(0) \approx \frac{1}{\sqrt{2 \pi n}}
  \]

- **Expected number of visits to the origin**:  
  \[
  \sum_{n=1}^\infty P_n(0) = \infty
  \]

Thus, in 1D, the random walk is **recurrent**: the walker will almost surely return to the origin infinitely often.

---

## Higher Dimensions
- **2D**: A similar derivation shows that the sum of return probabilities also diverges. Therefore, **2D walks are recurrent**.  
- **3D**: The sum converges to a finite value, which means there is a **nonzero probability of never returning**. Therefore, **3D walks are transient**.  

## Requirements

To run this project, you'll need the following Python libraries:

- `numpy`
- `matplotlib`

You can install them using `pip`:

```bash
pip install numpy matplotlib
