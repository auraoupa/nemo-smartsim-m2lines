#!/bin/bash
#SBATCH --job-name=nemo_driver
#SBATCH --time=00:15:00                          # Time limit hrs:min:sec
#SBATCH --nodes=1
#SBATCH --ntasks=40                    # Nombre total de processus MPI
#SBATCH --ntasks-per-node=40         # nombre de taches MPI par noeud
#SBATCH --hint=nomultithread        #  1 processus MPI par coeur physique (pas d'hyperthreading)
#SBATCH --output=test%j.out          # nom du fichier de sortie
#SBATCH --error=test%j.out           # nom du fichier d'erreur (ici en commun avec la sortie)
#SBATCH --qos=qos_cpu-dev
#SBATCH --account=eee@cpu

source /linkhome/rech/genige01/rote001/.bashrc
load_smart

set -x

cd /gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SMSIM
python driver_MED025.L75-JZAA001.py clustered
