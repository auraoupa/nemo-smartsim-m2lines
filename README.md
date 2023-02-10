# SmartSim with NEMO model

This work is part of M2LINES project and is done in collaboration with [Anastasia Gorbunova](https://github.com/anastasiaGor), [Andrew Shao](https://github.com/ashao) and [Julien LeSommer](https://github.com/lesommer)

We want to use [SmartSim](https://www.craylabs.org/docs/index.html) in coordination with [NEMO](https://www.nemo-ocean.eu/) to replace some parametrizations by machine learning inferences.

This work is done on IDRIS' Jean-Zay supercomputer

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

INPUTS and FORCINGS are gathered in separate repositories

 - The reference run [EXP00](https://github.com/auraoupa/nemo-smartsim-m2lines/tree/main/MED025.L75-JZAA001/EXP00) is done by running NEMO alone on 40 cores (1 node)

 - The first SmartSim experiment [EXP_SMSIM](https://github.com/auraoupa/nemo-smartsim-m2lines/tree/main/MED025.L75-JZAA001/EXP_SMSIM) is designed to reproduce the reference run with SmartSim orchestrator that launches also a database that will be later used to exchange data between NEMO and python and ML models
 
 - The second SmartSim experiment [EXP_SSINT]() does exactly the same than the previous test but interactively 
 
 ## New experiment
 
 Now I want to modify NEMO to include communications to the database, so I create a new experiment:
 
  - in NEMO tree, I add the line ```MED025.L75-JZAA002  OCE ICE``` to the work_cfgs.txt file
  - I ask for a compilation node on jean-zay with 
  ```
  srun --pty --ntasks=8 --cpus-per-task=1 --hint=nomultithread --partition=compil --time=00:20:00 --account=cli@cpu bash
  ```
  - I load the smartsim environment variables
  - then I run the compilation : ```./makenemo -r 'MED025.L75-JZAA002' -m 'X64_JEANZAY_smartsim```
  - I add the modifications to some NEMO routine in MY_SRC : 
