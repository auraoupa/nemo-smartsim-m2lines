#!/bin/bash

#SBATCH --output=/gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo.out
#SBATCH --error=/gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo.err
#SBATCH --job-name=nemo-COVMAPIKYSOD
#SBATCH --nodes=1
#SBATCH --time=00:15:00
#SBATCH --account=egi@cpu

cd /gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo_0 ; /gpfslocalsys/slurm/current/bin/srun --output /gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo_0/nemo_0.out --error /gpfsdswork/projects/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SSINT/NEMO-MEDITERR/nemo/nemo_0/nemo_0.err --job-name nemo_0-COVMAPJ0YCWW --export SSDB=10.148.4.133:6780,SSKEYIN=nemo_0,SSKEYOUT=nemo_0 /gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/BLD/bin/nemo.exe &

wait
