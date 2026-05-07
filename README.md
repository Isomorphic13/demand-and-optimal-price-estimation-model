This model implements estimation of the parameters $\alpha$ and $\epsilon$ in the log-linear demand model, where demand can be written as

$$\log(Q) = \beta_1 + \beta_2 \log(p)$$
or
$$Q = \alpha p^{-\epsilon}$$


Where $Q$ is demand in one year, $p$ price of the product and $\epsilon$ is elasticity (see: https://en.wikipedia.org/wiki/Elasticity_(economics)). \
\
To estimate the parameters we assume that each csutomer's demand follows Poisson distribution, where $\lambda = Q$, and with linearity of random variables from poisson distribution the market itself follows Poisson distribution. For the estimation we use baysian update for pairs ($\alpha$ , $\epsilon$) (see (https://en.wikipedia.org/wiki/Bayesian_inference). \
Thus with estimeted $\alpha$ and $\epsilon$ parameters we can calculate the optimal product price, if we consider inventory size (how much do we have now) and expairing date (the product will be gone after some time interval) problems. This is achieved by maximazing the expected value of profit for a given time. If on avarage we sell $\lambda = \alpha p ^ \epsilon" in one year we expect to sell $\lambda \frac{d}{365}$ units of a product in time interval $\frac{d}{365}$, where $d$ is day left before the expiration date. The inventory size $s$ truncates the expected amount of sold product units in the given time interval, because if the demand higher than inventory size, it't impossible to sell more. Thus it becomes:

$$E[units \ sold] = \sum_{k=0} ^s P(K = k)k + P(k > s) s$$
Where P is the probability of k units will be sold:
$$P(K = k) = \frac{e^ \lambda}{k!} \lambda ^k$$

Therefore our task is find $\max E$


