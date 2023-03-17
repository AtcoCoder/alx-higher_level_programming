#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product_list = [score * weight for (score, weight) in my_list]
    weights = [weight for (score, weight) in my_list]
    sum_of_product = sum(product_list)
    total_weight = sum(weights)
    average = sum_of_product / total_weight
    return average
