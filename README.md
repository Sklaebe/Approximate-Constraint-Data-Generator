Data generator to generate datasets with approximate constraints. Currently approximate sorting (ascending) and approximate uniqueness is supported.

The generated data consists of a unique key column and a value column fulfilling the intended constraint. The number of exceptions can be adjusted using the exception rate parameter. For the sorting constraint, exceptions form a descending sequence. For uniqueness constraint, exceptions form 100K groups. Exceptions are placed at random positions within the dataset.

Usage: 
```
gen.py -t <num_tuples> -e <exception_rate> -c <constraint(sort/unique)
```
