#!/bin/sh
#SBATCH --account=mecheng
#SBATCH --partition=curie
#SBATCH --nodes=1 --ntasks=64 --ntasks-per-node=64
#SBATCH --time=400:00:00
#SBATCH --job-name="generate_map"

# Modify the lines below for email alerts. Valid type values are NONE, BEGIN, END, FAIL, REQUEUE, ALL 
#SBATCH --mail-user=mlrchr001@myuct.ac.za
#SBATCH --mail-type=BEGIN,END,FAIL

# The cluster is configured primarily for OpenMPI and PMI. Use srun to launch parallel jobs if your code is parallel aware.
# To protect the cluster from code that uses shared memory and grabs all available cores the cluster has the following 
# environment variable set by default: OMP_NUM_THREADS=1
# If you feel compelled to use OMP then uncomment the following line:
# export OMP_NUM_THREADS=$SLURM_NTASKS

module load python/anaconda-python-3.7
python ../generate_map.py
