I also suppose learn about the pytorch, this is the way that our team want to use in the further project. So I tried the both link about VQA. First, I need to install Anaconda, I will use the 64-bit grapical installer for Pytorch. To install Pytorch with Anaconda, I will need to open an Anaconda prompt via Start|Anaconda3|Anaconda Prompt, to install Pytorch via Anaconda, and have a CUDA-capable system. Choose OS: Windows, Package: Conda and CUDA version suited to my machine. Run the Command: conda intall pytorch torchvision cudatoolkit=10.2 -c pytorch To ensure that PyTorch was installed correctly, we can verify the installation by running sample PyTorch code. Here we will construct a randomly initialized tensor. From the command line, type: "python" then enter the following code:

"from future import print_function import torch x = torch.rand(5, 3) print(x)"

The output should be something similar to: tensor([[0.3380, 0.3845, 0.3217], [0.8337, 0.9050, 0.2650], [0.2979, 0.7141, 0.9069], [0.1449, 0.1132, 0.1375], [0.4675, 0.3947, 0.1426]]) Additionally, to check if your GPU driver and CUDA is enabled and accessible by PyTorch, run the following commands to return whether or not the CUDA driver is enabled:

"import torch torch.cuda.is_available()"

Then, according to the github link: https://github.com/pytorch/examples/tree/master/word_language_model
