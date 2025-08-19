# DivideAndConcur

This repository contains plots showing the results of Divide and Concur run on selected problems.
The instances are base on the [NETLIB LP](https://www.netlib.org/lp/data/readme) collection and the 
SuiteSparse Matrix Collection, see
Timothy A. Davis and Yifan Hu. 2011. The University of Florida Sparse Matrix Collection. ACM Transactions on Mathematical Software 38, 1, Article 1 (December 2011), 25 pages. DOI: https://doi.org/10.1145/2049662.2049663

Further, this repository contains code to generate the plots in [GeneratePlots.py](./GeneratePlots.py).
This requires the precomputed erros in the .npz files.
These files can be generated with [ComputeRuns.py](./ComputeRuns.py), though this can take up to two hours.
