# SmartSim with NEMO model

This work is part of M2LINES project and is done in collaboration with [Anastasia Gorbunova](https://github.com/anastasiaGor), [Andrew Shao](https://github.com/ashao) and [Julien LeSommer](https://github.com/lesommer)

We want to use [SmartSim](https://www.craylabs.org/docs/index.html) in coordination with [NEMO](https://www.nemo-ocean.eu/) to replace some parametrizations by machine learning inferences.

This work is done on IDRIS' Jea-Zay supercomputer

## Installation

I followed [Anastasia's guidelines](https://github.com/anastasiaGor/nemo4-imhotep) and added a function in my .bashrc to load the proper environment :

```bash
load_smart()
{
        module load intel-all/2019.4
        module load hdf5/1.10.5-mpi
        module load netcdf/4.7.2-mpi
        module load python/3.8.8
 
        export PATH=/linkhome/rech/genige01/rote001/.local/bin:$PATH
        export PATH=/gpfswork/rech/eee/rote001/git/RedisAI/bin/linux-x64-release/install-cpu:$PATH
        export RAI_PATH=/gpfswork/rech/eee/rote001/git/RedisAI/bin/linux-x64-release/install-cpu/redisai.so

        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/gpfswork/rech/eee/rote001/git/smartredis/install/lib
        export SMARTREDIS_FORTRAN_SRC=/gpfswork/rech/eee/rote001/git/smartredis/src_fortran
        export SMARTREDIS_FORTRAN_SRC_FLAT=/gpfswork/rech/eee/rote001/git/smartredis/src_fortran_flat
}
```

We work with NEMO version 4.0.7 and a reduced configuration taken from the IMHOTEP project eORCA025.L75-IMHOTEP02 : MED025.L75 for testing purposes.

NEMO is compiled with smartredis library.

## First experiments

INPUTS and FORCINGS are gathered in separate 
The reference run EXP00 is done by running NEMO alone on 40 cores (1 node)

The first SmartSim experiment EXP_SMSIM is designed to reproduce the reference run with SmartSim orchestrator that launches also a database that will be later used to exchange data between NEMO and python and ML models
