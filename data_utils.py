
import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:

    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully loaded {file_path}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")
        return pd.DataFrame()


def summarize_data(df: pd.DataFrame) -> None:

    if df.empty:
        print("[WARNING] Empty DataFrame, nothing to summarize.")
        return

    print("\n--- Data Summary ---")
    print(f"Shape: {df.shape}")
    print("\nColumns:", list(df.columns))
    print("\nHead:\n", df.head())
    print("\nDescription:\n", df.describe())


if __name__ == "__main__":
    data = load_csv("sample.csv")
    summarize_data(data)
