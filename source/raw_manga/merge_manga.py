<<<<<<< HEAD
import pandas as pd

def merge_csv_files(file_paths, output_file):
    """
    Ghép nhiều file CSV lại thành một file CSV duy nhất với encoding utf-8-sig.
    
    Args:
        file_paths (list): Danh sách đường dẫn đến các file CSV cần ghép.
        output_file (str): Đường dẫn đến file CSV kết quả.
    """
    # Đọc và ghép các file CSV
    dfs = [pd.read_csv(file_path, encoding='utf-8-sig') for file_path in file_paths]
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Lưu file CSV mới
    merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Đã ghép {len(file_paths)} file CSV vào file: {output_file}")

# Danh sách các file CSV cần ghép
file_paths = ['raw_data/raw_manga_1.csv', 'raw_data/raw_manga_2.csv', 'raw_data/raw_manga_3.csv', 'raw_data/raw_manga_4.csv']

# Tên file kết quả
output_file = 'raw_data/raw_manga.csv'

# Gọi hàm
merge_csv_files(file_paths, output_file)
=======
import pandas as pd

def merge_csv_files(file_paths, output_file):
    """
    Ghép nhiều file CSV lại thành một file CSV duy nhất với encoding utf-8-sig.
    
    Args:
        file_paths (list): Danh sách đường dẫn đến các file CSV cần ghép.
        output_file (str): Đường dẫn đến file CSV kết quả.
    """
    # Đọc và ghép các file CSV
    dfs = [pd.read_csv(file_path, encoding='utf-8-sig') for file_path in file_paths]
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Lưu file CSV mới
    merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Đã ghép {len(file_paths)} file CSV vào file: {output_file}")

# Danh sách các file CSV cần ghép
file_paths = ['raw_data/raw_manga_1.csv', 'raw_data/raw_manga_2.csv', 'raw_data/raw_manga_3.csv', 'raw_data/raw_manga_4.csv']

# Tên file kết quả
output_file = 'raw_data/raw_manga.csv'

# Gọi hàm
merge_csv_files(file_paths, output_file)
>>>>>>> 745538bbac3bcf10b327562cf09bcc013fbbfa6a
