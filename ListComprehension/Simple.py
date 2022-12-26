[i for i,x in enumerate([1,2,3,2]) if x==2] # => [1, 3]

3 in [1, 2, 3] # => True


matches = [x for x in lst if fulfills_some_condition(x)]
matches = (x for x in lst if x > 6)

next((i for i, x in enumerate(lst) if [condition on x]), [default value])

pip3 install more-itertools


