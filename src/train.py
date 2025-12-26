import numpy as np
import json 
from pathlib import Path

print("Traininig model...")

data= np.random.rand(100)
mean=data.mean()

#Solo es una simulación

model= {
    "mean":float(mean),
    "version":"v1"
}

Path("artifacts").mkdir(exist_ok=True)


with open("artifacts/model.json","w") as f:
    json.dump(model,f)

print("Model saved!")