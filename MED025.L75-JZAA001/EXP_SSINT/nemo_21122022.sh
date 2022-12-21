#!/bin/bash

#SBATCH --output=/gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo.out
#SBATCH --error=/gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo.err
#SBATCH --job-name=nemo-CP7J5P8RLKWX
#SBATCH --ntasks=40
#SBATCH --partition=compil
#SBATCH --export=ALL
#SBATCH --nodes=1
#SBATCH --time=00:15:00
#SBATCH --account=egi@cpu
source /linkhome/rech/genige01/rote001/smart_path.ksh; module load intel-all/2019.4; module load hdf5/1.10.5-mpi; module load netcdf/4.7.2-mpi; ldd /gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/BLD/bin/nemo.exe

cd /gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo_0 ; /gpfslocalsys/slurm/current/bin/srun --output /gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo_0/nemo_0.out --error /gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo_0/nemo_0.err --job-name nemo_0-CP7J5P9O2GV4 --export SSDB=10.148.251.13:6780,SSKEYIN=nemo_0,SSKEYOUT=nemo_0 --ntasks-per-node=40 --ntasks=40 /gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/BLD/bin/nemo.exe &

wait
