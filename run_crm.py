
from __future__ import annotations

from pathlib import Path

import pandas as pd
from pywaterflood import CRM

TAU_SELECTION = "per-pair"
CONSTRAINTS = "up-to one"
NUM_CORES = 8
data_dir = Path("/data")
prod = pd.read_csv(data_dir / "production.csv", header=None).to_numpy()
inj = pd.read_csv(data_dir / "injection.csv", header=None).to_numpy()
time = pd.read_csv(data_dir / "time.csv", header=None).to_numpy()[:, 0]

for run in range(10):
    crm = CRM(tau_selection=TAU_SELECTION, constraints=CONSTRAINTS)
    crm.fit(prod, inj, time, num_cores=NUM_CORES, random=True)
    crm.to_pickle(Path("/results") / f"crm_results_{run}.pkl")

