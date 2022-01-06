def count_parameters(model):
    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total_params


def count_conv_flop(layer, x):
    out_h = int(x.size()[2] / layer.stride[0])
    out_w = int(x.size()[3] / layer.stride[1])
    delta_ops = layer.in_channels * layer.out_channels * layer.kernel_size[0] * layer.kernel_size[1] * \
                out_h * out_w / layer.groups
    return delta_ops

def count_mem(layer, x):
    return layer.weight.numel() + x.numel()

def hw_cost_conv(layer, x, metric):
    if metric == "flops":
        return count_conv_flop(layer, x)
    elif metric == "mem":
        return count_mem(layer, x)
    else:
        return NotImplementedError("invalid hw metric: "+str(metric))
    return count_hw_cost(layer, x)

def hw_cost_linear(layer, x, metric):
    if metric == "flops":
        return layer.weight.numel()
    elif metric == "mem":
        return count_mem(layer, x)
    else:
        return NotImplementedError("invalid hw metric:" + str(metric))