import numpy as np
import json
from pathlib import Path


# Simulación de datos
data = np.random.rand(100)
mean = data.mean()

# ----- MODELO (artifact) -----
model = {
    "mean": float(mean),
    "version": "v1"
}

Path("artifacts").mkdir(exist_ok=True)

with open("artifacts/model.json", "w") as f:
    json.dump(model, f)


# ----- MÉTRICA (output) -----
# SOLO key=value, nada más
print(f"mean={mean}")
