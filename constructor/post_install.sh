#!/bin/bash

source "$PREFIX/etc/profile.d/conda.sh"
conda activate "$PREFIX"

python -m pip install ImSwitchUC2
python -m pip install UC2-REST