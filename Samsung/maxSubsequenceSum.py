def find_max_sum(arr):
    in_, out_ = 0, 0
    for i in arr:
        if out_ > in_:
            new_out_ = out_
        else:
            new_out_ = in_
        in_ = out_ + i
        out_ = new_out_
    if out_ > in_:
        return out_
    return in_


arr = [5, 5, 10, 100, 10, 5]
print(find_max_sum(arr))
