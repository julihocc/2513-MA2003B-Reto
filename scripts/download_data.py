"""
Script to download sales data from Kaggle.
Dataset: dataregina/datasets-para-proyecto-bi
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import kagglehub
    import pandas as pd
    from tqdm import tqdm
except ImportError as e:
    print(f"Error: Missing required package: {e}")
    print("Please install required packages: pip install kagglehub pandas tqdm")
    sys.exit(1)


def download_kaggle_dataset():
    """Download dataset from Kaggle using kagglehub."""
    print("=" * 70)
    print("Downloading Sales Pattern Analysis Dataset from Kaggle")
    print("=" * 70)

    try:
        # Download dataset
        print("\n📥 Downloading dataset...")
        print("Dataset: dataregina/datasets-para-proyecto-bi")

        # Download latest version
        path = kagglehub.dataset_download("dataregina/datasets-para-proyecto-bi")

        print(f"\n Dataset downloaded to: {path}")

        return path

    except Exception as e:
        print(f"\n Error downloading dataset: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure you have Kaggle API credentials configured")
        print("2. Create ~/.kaggle/kaggle.json with your API key")
        print("3. Get API key from: https://www.kaggle.com/settings/account")
        print("4. kaggle.json format:")
        print('   {"username":"your_username","key":"your_api_key"}')
        return None


def explore_dataset(dataset_path):
    """Explore the downloaded dataset."""
    if not dataset_path or not os.path.exists(dataset_path):
        print("\n Dataset path not found")
        return

    print("\n" + "=" * 70)
    print("Exploring Downloaded Dataset")
    print("=" * 70)

    # List all files
    print(f"\n📁 Dataset location: {dataset_path}\n")

    dataset_dir = Path(dataset_path)
    files = list(dataset_dir.glob("*.csv"))

    if not files:
        print("  No CSV files found in dataset directory")
        return

    print(f"Found {len(files)} CSV file(s):\n")

    # Explore each file
    for file_path in tqdm(files, desc="Analyzing files"):
        print(f"\n{'' * 70}")
        print(f"📄 File: {file_path.name}")
        print(f"{'' * 70}")

        try:
            # Read first few rows
            df = pd.read_csv(file_path, nrows=5)

            # File info
            full_df = pd.read_csv(file_path)
            print(f"📊 Shape: {full_df.shape[0]:,} rows × {full_df.shape[1]} columns")
            print(f"💾 Size: {file_path.stat().st_size / 1024:.2f} KB")

            # Column info
            print(f"\n📋 Columns ({len(full_df.columns)}):")
            for idx, col in enumerate(full_df.columns, 1):
                dtype = full_df[col].dtype
                null_count = full_df[col].isna().sum()
                null_pct = (null_count / len(full_df)) * 100
                print(f"  {idx:2d}. {col:30s} | {str(dtype):10s} | Nulls: {null_count:6,} ({null_pct:5.2f}%)")

            # Preview
            print(f"\n👁️  Preview (first 3 rows):")
            print(df.head(3).to_string(index=False))

            # Basic stats for numeric columns
            numeric_cols = full_df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                print(f"\n📈 Numeric column statistics:")
                print(full_df[numeric_cols].describe().round(2).to_string())

        except Exception as e:
            print(f"  Error reading file: {e}")

    print("\n" + "=" * 70)
    print(" Dataset exploration complete!")
    print("=" * 70)


def copy_to_project_data(dataset_path):
    """Copy downloaded data to project data/raw directory."""
    if not dataset_path:
        return

    print("\n" + "=" * 70)
    print("Copying Data to Project Directory")
    print("=" * 70)

    # Get project data directory
    project_root = Path(__file__).parent.parent
    raw_data_dir = project_root / "data" / "raw"
    raw_data_dir.mkdir(parents=True, exist_ok=True)

    # Copy files
    dataset_dir = Path(dataset_path)
    csv_files = list(dataset_dir.glob("*.csv"))

    if not csv_files:
        print("\n  No CSV files to copy")
        return

    import shutil

    print(f"\n📂 Copying {len(csv_files)} file(s) to: {raw_data_dir}\n")

    for file_path in csv_files:
        dest_path = raw_data_dir / file_path.name
        shutil.copy2(file_path, dest_path)
        print(f"   Copied: {file_path.name}")

    print(f"\n All files copied to: {raw_data_dir}")


def main():
    """Main function."""
    print("\n🚀 Starting Data Download Process\n")

    # Download dataset
    dataset_path = download_kaggle_dataset()

    if dataset_path:
        # Explore dataset
        explore_dataset(dataset_path)

        # Copy to project directory
        copy_to_project_data(dataset_path)

        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Data download and setup complete")
        print("=" * 70)
        print(f"\n📍 Data location: data/raw/")
        print("\n📝 Next steps:")
        print("  1. Review data in data/raw/")
        print("  2. Create data dictionary (docs/data_dictionary.md)")
        print("  3. Start data quality assessment")
        print("\n")
    else:
        print("\n" + "=" * 70)
        print(" Data download failed")
        print("=" * 70)
        print("\nPlease configure Kaggle API credentials and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
