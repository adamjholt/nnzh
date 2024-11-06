# Neural Networks: Zero to Hero

Working through [Andrej Karpathys course](https://github.com/karpathy/nn-zero-to-hero) on neural networks.

## Lecture 1: The spelled-out intro to neural networks and backpropagation: building micrograd

__What is [micrograd](https://github.com/karpathy/micrograd)?__ A tiny scalar-valued autograd engine that implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API. In other words, it's a super simple mini Pytorch _without_ the complexities of dealing with tensors.

__What is autograd?__ Automatic gradient, a system that automatically tracks mathematical operations and builds a computation graph of those operations, i.e., the DAG (directed acyclic graph).

__What is backpropagation?__ An algorithm that computes the gradients (derivates) of the loss function with respect to the weights of the neural network. Used to tune the weights during training in order to minimize the loss. It works by applying the chain rule backwards from the output of the network, through each layer, to the inputs. Note that backpropagation is a general algorithm not limited to neural networks.

__What is a loss function?__ A function that measures the difference between the neural network outputs and the correct values. In simple terms, a loss function tracks the degree of error in the model's outputs.

__What is a gradient?__ In neural networks, a gradient is a vector of partial derivatives of the loss function with respect to the model’s weights and biases.  It indicates the direction and magnitude of the steepest increase in error, allowing _gradient descent_ to adjust in the opposite direction to optimize (minimize) loss.

__What is a vector?__

__What is a derivative?__

__Why partial derivatives?__

__What is a neural network?__


