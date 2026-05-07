This model implements estimation of the parameters $\alpha$ and $\epsilon$ in the log-linear demand model, where demand can be written as

$$\log(Q) = \beta_1 + \beta_2 \log(p)$$
or
$$Q = \alpha p^{-\epsilon}$$


Where $Q$ is demand in one year, $p$ price of the product and $\epsilon$ is elasticity (see: https://en.wikipedia.org/wiki/Elasticity_(economics)). \
\
To estimate the parameters we assume that each csutomer's demand follows Poisson distribution, where $\lambda = Q$, and with linearity of random variables from poisson distribution the market itself follows Poisson distribution. For the estimation we use baysian update for pairs ($\alpha$ , $\epsilon$) (see (https://en.wikipedia.org/wiki/Bayesian_inference). \
Thus with estimeted $\alpha$ and $\epsilon$ parameters we can calculate the optimal product price, if we consider inventory size (how much do we have now) and expairing date (the product will be gone after some time interval) problems


