# alpha_stab_levy__sym_disc

This code generates symmetric alpha stable Levy process paths.

The statement of Proposition 1.7.1 in Gennady Samorodnitsky, Murad Taqqu states that if $\gamma$ has uniform distribution on $(-\pi/2,\pi/2)$ and $W$ follows a standard exponential law, then the random quantity
$$X=\frac{\sin(\alpha \gamma)}{\cos(\gamma)^{1/\alpha}}(\frac{\cos((1.\alpha)\gamma)}{W})^{\frac{1-\alpha}{\alpha}}$$
has a symmetric, non-skewed, and centered $\alpha$-stable law.

Using properties of Levy processes, and the fact that in case of Levy processes stable marginals imply self-similarity, simulation can be done with minor effort.

References.
Gennady Samorodnitsky, Murad Taqqu - Stable Non-Gaussian Random Processes_ Stochastic Models with Infinite Variance (Stochastic Modeling Series)-Chapman and Hall_CRC (1994)
