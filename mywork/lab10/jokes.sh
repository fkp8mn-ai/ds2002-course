#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --partition=standard
#SBATCH --job-name=lolcow
#SBATCH --output=lolcow_%j.out
#SBATCH --error=lolcow_%j.err
#SBATCH --time=0:01:00
#SBATCH --mem=8GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-10

# Load Apptainer
module load apptainer

# Run the lolcow container
apptainer run ~/lolcow-latest.sif
