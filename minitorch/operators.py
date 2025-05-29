"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y


def id(x: float) -> float:
    """Identity function."""
    return x


def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y


def neg(x: float) -> float:
    """Negate a number."""
    return -x


def lt(x: float, y: float) -> bool:
    """Check if x is less than y."""
    return x < y


def eq(x: float, y: float) -> bool:
    """Check if x is equal to y."""
    return x == y


def max(x: float, y: float) -> float:
    """Return the maximum of two numbers."""
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    """Check if two numbers are close to each other."""
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    """Compute the sigmoid function."""
    if x >= 0:
        return 1.0 / (1.0 + exp(-x))
    else:
        return exp(x) / (1.0 + exp(x))


def relu(x: float) -> float:
    """Compute the ReLU function."""
    return max(0, x)


def log(x: float) -> float:
    """Compute the natural logarithm."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(x)


def exp(x: float) -> float:
    """Compute the exponential function."""
    return math.exp(x)


def log_back(x: float, y: float) -> float:
    """Compute the derivative of the logarithm times y."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return y / x  # Derivative of log(x) is 1/x


def inv(x: float) -> float:
    """Compute the inverse of a number."""
    if x == 0:
        raise ValueError("Inverse undefined for zero.")
    return 1 / x


def inv_back(x: float, y: float) -> float:
    """Compute the derivative of the inverse function times y."""
    if x == 0:
        raise ValueError("Inverse undefined for zero.")
    return -y / (x**2)  # Derivative of 1/x is -1/x^2


def relu_back(x: float, y: float) -> float:
    """Compute the derivative of the ReLU function times y."""
    return y if x > 0 else 0  # Derivative of ReLU is 1 for x > 0, else 0


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
