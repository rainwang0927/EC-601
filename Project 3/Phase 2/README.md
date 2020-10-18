I also suppose learn about the pytorch, this is the way that our team want to use in the further project. So I tried the Tensorflow for phase 1 and pytorch for phase 2. 
First, I need to install Anaconda, I will use the 64-bit grapical installer for Pytorch. 
To install Pytorch with Anaconda, I will need to create a new environment in Anaconda, and then open an Anaconda prompt via Start|Anaconda3|Anaconda Prompt, to install Pytorch via Anaconda, and have a CUDA-capable system. Choose OS: Windows, Package: Conda and CUDA version suited to my machine. Run the Command: conda intall pytorch torchvision cudatoolkit=10.2 -c pytorch To ensure that PyTorch was installed correctly, we can verify the installation by running sample PyTorch code. Here we will construct a randomly initialized tensor. From the command line, type: "python" then enter the following code:

"from future import print_function import torch x = torch.rand(5, 3) print(x)"

The output should be something similar to: tensor([[0.3380, 0.3845, 0.3217], [0.8337, 0.9050, 0.2650], [0.2979, 0.7141, 0.9069], [0.1449, 0.1132, 0.1375], [0.4675, 0.3947, 0.1426]]) Additionally, to check if your GPU driver and CUDA is enabled and accessible by PyTorch, run the following commands to return whether or not the CUDA driver is enabled:

"import torch torch.cuda.is_available()"

As my GPU is RTX 2070 super, it is good to run it.

Then, according to the github link: https://github.com/pytorch/examples/tree/master/word_language_model, use the raw data from the wikitext-2 dataset. See https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/
This example trains a multi-layer RNN on a language modeling task. The trained model can then be used by the generate script to generate new text.
This model uses the nn.RNN model(and its sister modules nn.GRU and nn.LSTM) which will automatically use the cuDNN backend if run on CUDA with cuDNN installed.
A variety of models can bne tested, as an exmaple, the following arguments produce slower but better models:

python main.py --cuda --emsize 650 --nhid 650 --dropout 0.5 --epochs 40           
python main.py --cuda --emsize 650 --nhid 650 --dropout 0.5 --epochs 40 --tied    
python main.py --cuda --emsize 1500 --nhid 1500 --dropout 0.65 --epochs 40        
python main.py --cuda --emsize 1500 --nhid 1500 --dropout 0.65 --epochs 40 --tied 

I used python main.py --cuda to run the full models. I uploade the procedure as Procedure.txt. In this file, we can easily found that it totally run 40 epoch and 2983 batches each epoch. Compare with each epoch, the time, valid loss and valid ppl is contineously decreasing, which shows that it is keep doing the machine learing. As compared, first epoch, time: 59.23s, valid loss 5.55, valid ppl 256.40. Last epoch, time: 44.32s, valid loss 4.74, valid ppl 114.17.

After it run 40 epoch, it will end the program. Then enter the python generate.py, it will generate samples from the trained LSTM model. I uploaded it as generated.txt


