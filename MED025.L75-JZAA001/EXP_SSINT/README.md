# Launch NEMO via SmartSim interactively (on jupyter notebook)

  - request a visu node on which the notebook will be launched : 
```
salloc --ntasks=1 --cpus-per-task=5 --account=egi@cpu --partition=prepost --time=05:00:00 srun --pty bash
```
  - load the smartsim environment : ```load_smart```
  - lauch the jupyterhub :
```
idrlab --notebook-dir=/gpfswork/rech/eee/rote001/nemo4-imhotep-main
```


