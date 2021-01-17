import torch
from tqdm import tqdm
import torch.nn.functional as F
from torch.optim.lr_scheduler import StepLR, ReduceLROnPlateau

from config.optimizer import Optimizer
from model.ghostnet import GhostNet
from model.plain_old_model import PlainOldNet


class ModelLearning():
    def __init__(self):
        self.train_losses = []
        self.test_losses = []
        self.train_acc = []
        self.test_acc = []
        self.misclassified = []

    def __train(self, model, device, train_loader, optimizer, l1_enabled):
        model.train()
        pbar = tqdm(train_loader, position = 0, leave = True)
        correct = 0
        processed = 0
        for batch_idx, (data, target) in enumerate(pbar):
            # get samples
            data, target = data.to(device), target.to(device)
            # Init
            optimizer.zero_grad()
            # In PyTorch, we need to set the gradients to zero before starting to do backpropragation because PyTorch accumulates the gradients on subsequent backward passes. 
            # Because of this, when you start your training loop, ideally you should zero out the gradients so that you do the parameter update correctly.
            
            # Predict
            y_pred = model(data)
            loss = F.nll_loss(y_pred, target)

            # Calculate loss
            if l1_enabled:
                lambda_l1 = 0.0001
                l1 = 0
                for p in model.parameters():
                    l1 = l1 + p.abs().sum()
                    loss = loss + lambda_l1*l1
            
            self.train_losses.append(loss)

            # Backpropagation
            loss.backward()
            optimizer.step()

            # Update pbar-tqdm
    
            pred = y_pred.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()
            processed += len(data)

            pbar.set_description(desc= f'Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}')
            self.train_acc.append(100*correct/processed)

    def __test(self, model, device, test_loader):
        model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in test_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
                pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability

                for focussed_data, prediction, actual in zip(data, pred, target):
                    if prediction != actual:
                        self.misclassified.append([focussed_data.cpu(), prediction[0], actual])


                correct += pred.eq(target.view_as(pred)).sum().item()


        test_loss /= len(test_loader.dataset)
        self.test_losses.append(test_loss)

        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
            test_loss, correct, len(test_loader.dataset),
            100. * correct / len(test_loader.dataset)))
    
        self.test_acc.append(100. * correct / len(test_loader.dataset))

    
    def start(self, device, epochs, learning_rate, scheduler_enabled, step_size, sc_gamma, train_loader, test_loader):
        
        list_modes = ['gbn', 'l1_l2_gbn', 'l1_bn', 'l2_bn', 'l1_l2_bn']
        graph_plot_dict = dict()

        for mode in list_modes:

            print(f'---------------------Mode : {mode}---------------------')

            self.train_losses = []
            self.test_losses = []
            self.train_acc = []
            self.test_acc = []
                        
            model = GhostNet().to(device) if mode is 'gbn' or 'l1_l2_gbn' else PlainOldNet().to(device)
            
            optimizer = Optimizer.getOptimizer('l1_bn', model.parameters(), 0.02)
            scheduler = StepLR(optimizer, step_size=step_size, gamma= sc_gamma, verbose = True) if scheduler_enabled else None


            l1_enabled = True if mode is 'l1_l2_gbn' or 'l1_bn' or 'l1_l2_bn' else False
            
            for epoch in range(1, epochs+1):
                print(f'Epoch {epoch}')
                self.__train(model, device, train_loader, optimizer, l1_enabled)
                self.__test(model, device, test_loader)
                if(scheduler_enabled):
                    scheduler.step()
            
            graph_plot_dict[mode] = {
                "train_losses" : self.train_losses,
                "train_acc" : self.train_acc,
                "test_acc" : self.test_acc,
                "test_losses" : self.test_losses
            }

            print("--------------------------------------------------------")
            # misguided_pred_plot(self.misclassified)
        return graph_plot_dict

