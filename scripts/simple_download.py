import kagglehub
from pathlib import Path
import shutil

print("Downloading dataset...")
path = kagglehub.dataset_download("dataregina/datasets-para-proyecto-bi")
print(f"Downloaded to: {path}")

# Copy to data/raw
raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

files = list(Path(path).glob("*.csv"))
print(f"\nCopying {len(files)} files...")

for file in files:
    dest = raw_dir / file.name
    shutil.copy2(file, dest)
    print(f"  {file.name}")

print(f"\nDone! Files in: {raw_dir}")
