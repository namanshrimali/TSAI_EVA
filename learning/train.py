from tqdm import tqdm
import torch
import torch.nn as nn
import torch.optim as optim


def train(model, device, train_loader, epoch, learning_rate= 0.01):
    correct = 0
    processed = 0
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
    model.train()
    criterion = nn.CrossEntropyLoss()
    pbar = tqdm(train_loader, position = 0, leave = True)
    
    for batch_idx, (data, target) in enumerate(pbar):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        
        # Predict
        output = model(data)
        

        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        pred = output.argmax(dim=1, keepdim=True)
        correct += pred.eq(target.view_as(pred)).sum().item()
        processed += len(data)


        pbar.set_description(desc= f' Epoch = {epoch+1} loss={loss.item()} batch_id={batch_idx}')
    
    print('\Train set: Accuracy: {}/{} ({:.4f}%)\n'.format(
        correct, len(train_loader.dataset),
        100. * correct / len(train_loader.dataset)))