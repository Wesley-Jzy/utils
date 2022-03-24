from plot.plot import plot


# read data
def read_data(file, num_line=100):
    res = []
    offset = len('Loss = ')
    with open(file, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            start = line.find('Loss')
            end = line.find(' | Throughput')
            data = line[start+offset:end]
            res.append(data)
            if len(res) >= num_line:
                break
    return res


# process data
def process_data(train_data):
    x = range(len(train_data))
    y = train_data
    return x, y


def main():
    train_file = './data/bert_small_torch_batch16_epoch10000_step20_20220323_train.log'
    valid_file = './data/bert_small_torch_batch16_epoch10000_step20_20220323_valid.log'
    
    train_data = read_data(train_file, num_line=200)
    train_x, train_y = process_data(train_data)
    
    X = [train_x]
    Y = [train_y]
    xlabel = 'step'
    ylabel = 'Loss'
    legend = [f'Train']
    
    plot(X=X, Y=Y, xlabel=xlabel, ylabel=ylabel, legend=legend,figsize=(3.5, 2.5), save=False, save_path=None)


main()


