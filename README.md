## Neural Networks: Zero to Hero

Working through [Andrej Karpathys course](https://github.com/karpathy/nn-zero-to-hero) on neural networks.

### Lecture 1: The spelled-out intro to neural networks and backpropagation: building micrograd

>_Micrograd is basically an autograd engine. Autograd is short for automatic gradient and really what it does is it implements backpropagation. Now backpropagation is this algorithm that allows you to efficiently evaluate the gradient of some kind of loss function with respect to the weights of a neural network. And what that allows us to do then is we can iteratively tune the weights of that neural network to minimize the loss function and therefore improve the accuracy of the network. So back propagation would be at the mathematical core of any modern deep neural network library like say Pytorch._
>
> – Andrej Karpathy

__What is [micrograd](https://github.com/karpathy/micrograd)?__
A tiny scalar-valued autograd engine that implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API. In other words, it's a super simple mini Pytorch _without_ the complexities of dealing with tensors.

__What is autograd?__
Automatic gradient, a system that automatically tracks mathematical operations and builds a computation graph of those operations, i.e., a DAG (directed acyclic graph).

__What is backpropagation?__
An efficient way to compute gradients of a scalar loss with respect to many parameters by applying the chain rule in reverse through the computation graph (reverse-mode autodiff).

__What is a loss function?__
A scalar function that measures how wrong the model’s predictions are. Training tries to minimize this value over the dataset.

__What is a gradient?__
A vector of partial derivatives indicating how the function changes with respect to each input/parameter. For optimization, it points in the direction of steepest increase (so you move opposite to it for gradient descent).

__What is a vector?__
An ordered list of numbers that represents quantities like parameters or gradients in parameter space.

What is a derivative?
A number that describes how a function changes when its input changes by a tiny amount (rate of change). For multi-variable functions, that idea becomes partial derivatives.

__Why partial derivatives?__
Because most functions depend on multiple variables/parameters. Partial derivatives quantify sensitivity with respect to one variable while holding the others fixed, enabling gradient-based optimization.

__What is a neural network?__
A function approximator built from layers of simple differentiable computations (e.g., weighted sums plus nonlinearities). It has parameters (weights/biases) learned by minimizing a loss using backpropagation.

__What is gradient descent?__
Gradient descent is an optimization algorithm that updates parameters in the opposite direction of the gradient of a loss function to reduce it (hence _desent_).

If parameters are \(\theta\) and loss is \(L(\theta)\), a single update step is:

```math
\theta \leftarrow \theta - \alpha \nabla_\theta L(\theta)
```
where:
- \(\nabla_\theta L(\theta)\) is the gradient of the loss w.r.t. the parameters
- \(\alpha\) is the learning rate (step size)

