This model implements estimation of the parameters $\alpha$ and $\epsilon$ in the log-linear demand model for a single product, in which demand can be written as

$$\log(Q) = \beta_1 + \beta_2 \log(p)$$
or
$$Q = \alpha p^{\epsilon}$$


Where $Q$ is demand for a product in one year, $p$ is the price of the product and $\epsilon$ is elasticity (see: https://en.wikipedia.org/wiki/Elasticity_(economics)). \
\
To estimate the parameters, we assume that each customer's demand follows Poisson distribution, where $\lambda = Q$, and with linearity of random variables from poisson distribution the market itself follows Poisson distribution (see: https://en.wikipedia.org/wiki/Poisson_distribution). For the estimation of market's parameters we use Baysian updating to get a probability distribution for pairs ($\alpha$ , $\epsilon$) (see https://en.wikipedia.org/wiki/Bayesian_inference). Further for simplification we use single values $\alpha, \epsilon$ derived from the result of weighted sum from this distribution.\
Thus with the derived $\alpha$ and $\epsilon$ parameters of the market we can calculate the optimal product price, if we consider inventory size (how many product units to sell we have now) and expairing date (the product will be gone after some time interval) problems. This is achieved by maximazing the expected value of profit for a given time interval. If on avarage we sell $\lambda = \alpha p ^ \epsilon$ in one year, we expect to sell $\lambda d$ / $365$ units of a product in time interval $d$ / $365$, where $d$ is days left before the expiration date (we assume that the demand is uniformly ditributed over year). The inventory size $s$ truncates the expected amount of sold product units in the given time interval, because if the demand is higher than inventory size, it is impossible to sell more. Thus it becomes:

$$E[units \ sold] = \sum_{k=0} ^s P(K = k)k + P(K > s) s$$
Where P is the probability of k units will be sold:
$$P(K = k) = \frac{e^ \lambda}{k!} \lambda ^k$$

Therefore our task is to find $\max E[units \ sold]$ with the parameters $d,s$. \
Furthermore to verify the result of the model, we use monte carlo simulations (see: https://en.wikipedia.org/wiki/Monte_Carlo_method) for the Bayesian updating and the optimal price in main.py.




