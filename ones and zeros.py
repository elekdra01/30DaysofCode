def binary_array_to_number(arr):
    l=len(arr)
    s=0
    for i in range(l):
        if(arr[i]==1):
            s+=2**(l-1-i)
    return s
  # your code