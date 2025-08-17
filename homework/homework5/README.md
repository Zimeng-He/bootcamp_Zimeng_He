# Data Storage Utilities

## .env Paths
Typical usage defines variables such as "RAW" for raw data, "PROC" for processed data, "STARTER" for the sample DataFrame.

## Formats: CSV vs Parquet
- **CSV** is widely supported and easy to use, but produces larger files and loses type information.  
- **Parquet** is efficient, supports compression, and preserves schema, but requires additional libraries (`pyarrow` or `fastparquet`).  

In practice, CSV is better for small datasets and sharing across tools, while Parquet is recommended for larger datasets and internal pipelines.  

## Utilities
- **`detect_format(path)`** — infers file format from the file extension.  
- **`write_df(df, path)`** — writes a DataFrame to the specified location, creating parent folders automatically.  
- **`read_df(path)`** — reads a DataFrame back, parsing a `date` column automatically if present.  

## Validation and Assumptions
- Validation helpers confirm that data written and read back are equivalent.  
- CSV files are assumed to possibly contain a `date` column, which is parsed automatically.  
- If environment variables are not defined, the code falls back to default local directories.  
  
