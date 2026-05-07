import numpy
import numpy as np
import scipy.special
import scipy.stats as stats
from scipy import special


class BayesianUpdater:
    """
    Estimates alpha and epsilon of the market with Bayesian updating every day.
    See:
    https://en.wikipedia.org/wiki/Log%E2%80%93log_plot
    https://math.mit.edu/~dav/05.dir/class11-prep.pdf
    """
    def __init__(self, alphas: list, epsilons: list):
        # Store as NumPy array from the start
        self.alphas = np.array(alphas)
        self.epsilons = np.array(epsilons)
        self.grid = self.create_grid(self.alphas, self.epsilons)

    def create_grid(self, alphas, epsilons) -> numpy.ndarray:
        """
        Creates grid whose rows represent a triplet (alpha, epsilon, probability):
        a pair of parameters and the probability that this pair represents the true market's parameters
        """

        A, E = np.meshgrid(alphas, epsilons, indexing='ij')
        initial_prob = 1.0 / (len(alphas) * len(epsilons))
        grid = np.column_stack([A.ravel(), E.ravel(), np.full(A.size, initial_prob)])
        return grid

    def bayesian_update(self, bought_amount, price):
        """
        Implementation of bayesian updating for pairs of alphas and epsilons.
        """

        # working this logs to avoid total probability = 0
        log_priors = np.log(self.grid[:, 2] + 1e-300)
        mu_daily = (self.grid[:, 0] * (price ** self.grid[:, 1])) / 365

        # Vectorized likelihood
        log_likelihoods = stats.poisson.logpmf(k=bought_amount, mu=mu_daily)

        # Bayesian update in log-space
        log_unnormalized_posterior = log_priors + log_likelihoods
        log_total_evidence = special.logsumexp(log_unnormalized_posterior)

        # Update probabilities in the grid
        self.grid[:, 2] = np.exp(log_unnormalized_posterior - log_total_evidence)

    def get_weighted_results(self) -> float:
        """
        While bayesian update gives distribution for parameter, this method return single value for the parameters with respect to their probabilistic weight.
        :return: alpha and epsilon of the market.
        """

        # 1. Reshape the flat probability column using internal alpha/epsilon lengths
        # We use len(self.alphas) instead of passing it as an argument
        probs_matrix = self.grid[:, 2].reshape(len(self.alphas), len(self.epsilons))

        # 2. Sum the matrix along axes to get marginal probabilities
        # axis=1 sums across epsilons (giving total prob per alpha)
        # axis=0 sums across alphas (giving total prob per epsilon)
        marginal_alpha_probs = probs_matrix.sum(axis=1)
        marginal_epsilon_probs = probs_matrix.sum(axis=0)

        # 3. Calculate weighted averages using dot products
        alpha_weighted = np.dot(marginal_alpha_probs, self.alphas)
        epsilon_weighted = np.dot(marginal_epsilon_probs, self.epsilons)

        return alpha_weighted, epsilon_weighted





