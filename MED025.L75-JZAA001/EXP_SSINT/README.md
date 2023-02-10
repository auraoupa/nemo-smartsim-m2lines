# Launch NEMO via SmartSim interactively (on jupyter notebook)

## Old procedure with idrjup

  - request a visu node on which the notebook will be launched : 
```
salloc --ntasks=1 --cpus-per-task=5 --account=egi@cpu --partition=prepost --time=05:00:00 srun --pty bash
```
  - load the smartsim environment : ```load_smart```
  - lauch the jupyterhub :
```
idrlab --notebook-dir=/gpfswork/rech/eee/rote001/nemo4-imhotep-main
```

## New procedure with jupyterhub

  - on a machine that is recognized by Jean-Zay (or via tunnel to cal1) go to the webpage https://jupyterhub.idris.fr
  - enter your jean-zay credentials
  - select the SLURM spawner options
  - add the Environment variables : 
``` RAI_PATH=/gpfswork/rech/eee/rote001/git/RedisAI/bin/linux-x64-release/install-cpu/redisai.so
SMARTREDIS_FORTRAN_SRC=/gpfswork/rech/eee/rote001/git/smartredis/src_fortran
SMARTREDIS_FORTRAN_SRC_FLAT=/gpfswork/rech/eee/rote001/git/smartredis/src_fortran_flat``` 
  - choose 1 node, 1 task, the CPU partition, the qos_cpu-dev qos, the time and notebook directory

