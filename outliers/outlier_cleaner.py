#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here
    errors = [abs(p-n) for p,n in zip(predictions, net_worths)]
    cleaned_data = sorted([(a,n,e) for a,n,e in zip(ages, net_worths, errors)], key=lambda i: i[2])
    cleaned_data = cleaned_data[:len(cleaned_data)/10*9]
    
    return cleaned_data

