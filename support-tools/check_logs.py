import os

def scan_log(file_path: str) -> None:
    """Scan a log file and print lines containing ERROR or FAILED."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    error_count = 0
    with open(file_path, "r") as f:
        for line_num, line in enumerate(f, start=1):
            upper = line.upper()
            if "ERROR" in upper or "FAILED" in upper:
                print(f"[ISSUE] Line {line_num}: {line.strip()}")
                error_count += 1

    print(f"\nScan complete. Issues found: {error_count}")

if __name__ == "__main__":
    # For the lab, look for a simple sample_log.txt in the same folder
    scan_log("sample_log.txt")
