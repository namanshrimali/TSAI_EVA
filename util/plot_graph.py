import matplotlib.pyplot as plt

def plot_me_senpai(graph_plot_dict):
    print((graph_plot_dict.get("gbn")["test_losses"])
    (graph_plot_dict.get("gbn")["test_acc"]
    # fig, axs = plt.subplots(2,2,figsize=(15,10))

    # axs[0,0].plot(graph_plot_dict.get("gbn")["train_losses"])
    # axs[0,0].plot(graph_plot_dict.get("l1_l2_gbn")["train_losses"])
    # axs[0,0].plot(graph_plot_dict.get("l1_bn")["train_losses"])
    # axs[0,0].plot(graph_plot_dict.get("l2_bn")["train_losses"])
    # axs[0,0].plot(graph_plot_dict.get("l1_l2_bn")["train_losses"])
    # axs[0,0].set_title("Training Loss")
    # axs[0,0].legend(['gbn', 'l1_l2_gbn', 'l1_bn', 'l2_bn', 'l1_l2_bn'])

    # axs[0,1].plot(graph_plot_dict.get("gbn")["test_losses"])
    # axs[0,1].plot(graph_plot_dict.get("l1_l2_gbn")["test_losses"])
    # axs[0,1].plot(graph_plot_dict.get("l1_bn")["test_losses"])
    # axs[0,1].plot(graph_plot_dict.get("l2_bn")["test_losses"])
    # axs[0,1].plot(graph_plot_dict.get("l1_l2_bn")["test_losses"])
    # axs[0, 1].set_title("Test Loss")
    # axs[0,1].legend(['gbn', 'l1_l2_gbn', 'l1_bn', 'l2_bn', 'l1_l2_bn'])



    
    # axs[1, 0].plot(graph_plot_dict.get("gbn")["train_acc"])
    # axs[1, 0].plot(graph_plot_dict.get("l1_l2_gbn")["train_acc"])
    # axs[1, 0].plot(graph_plot_dict.get("l1_bn")["train_acc"])
    # axs[1, 0].plot(graph_plot_dict.get("l2_bn")["train_acc"])
    # axs[1, 0].plot(graph_plot_dict.get("l1_l2_bn")["train_acc"])
    # axs[1, 0].set_title("Training Accuracy")
    # axs[1, 0].legend(['gbn', 'l1_l2_gbn', 'l1_bn', 'l2_bn', 'l1_l2_bn'])


    
    # axs[1, 1].plot(graph_plot_dict.get("gbn")["test_acc"])
    # axs[1, 1].plot(graph_plot_dict.get("l1_l2_gbn")["test_acc"])
    # axs[1, 1].plot(graph_plot_dict.get("l1_bn")["test_acc"])
    # axs[1, 1].plot(graph_plot_dict.get("l2_bn")["test_acc"])
    # axs[1, 1].plot(graph_plot_dict.get("l1_l2_bn")["test_acc"])
    # axs[1, 1].set_title("Testing Accuracy")
    # axs[1,1].legend(['gbn', 'l1_l2_gbn', 'l1_bn', 'l2_bn', 'l1_l2_bn'])


    # fig.legend(['gbn', 'l1_l2_gbn', 'l1_bn', 'l2_bn', 'l1_l2_bn'])

    # # axs[0, 0].set_title("Training Loss")

    # # axs[1, 0].plot(train_acc[4000:], label=label)
    # # axs[1, 0].set_title("Training Accuracy")
    # # axs[0, 1].plot(test_losses, label= label)
    # # axs[0, 1].set_title("Test Loss")
    # # axs[1, 1].plot(test_acc, label = label)
    # # axs[1, 1].set_title("Test Accuracy")
    # fig.show()