#!/bin/bash
#SBATCH --job-name=nemo_test              # nom du job
#SBATCH --ntasks=40                    # Nombre total de processus MPI
#SBATCH --ntasks-per-node=40         # nombre de taches MPI par noeud
#SBATCH --hint=nomultithread        #  1 processus MPI par coeur physique (pas d'hyperthreading)
#SBATCH --time=00:15:00             # temps d execution maximum demande (HH:MM:SS)
#SBATCH --output=nemo_test%j.out          # nom du fichier de sortie
#SBATCH --error=nemo_test%j.out           # nom du fichier d'erreur (ici en commun avec la sortie)
#SBATCH --qos=qos_cpu-dev
#SBATCH --account=cli@cpu
 
cd /gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP00
# echo des commandes lancees
set -x

srun ./nemo 
#srun --mpi pmi2 --distribution=arbitrary -K1 --multi-prog ./ztask_file.conf
