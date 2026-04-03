import argparse
import hashlib
import json
import logging
import os
import sys
from datetime import datetime

# ---------------------------------------------------------
# Configure Logging
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

SUPPORTED_ALGOS = hashlib.algorithms_available


# ---------------------------------------------------------
# hash_file()
# ---------------------------------------------------------
def hash_file(path, algorithm="sha256"):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    if algorithm not in SUPPORTED_ALGOS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hasher = hashlib.new(algorithm)

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


# ---------------------------------------------------------
# save_output()
# ---------------------------------------------------------
def save_output(output_path, data):
    try:
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Results saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save output: {e}")


# ---------------------------------------------------------
# main()
# ---------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="File Hash Generator - Production Style"
    )

    parser.add_argument(
        "-f", "--file",
        required=True,
        help="Path to the file to hash"
    )

    parser.add_argument(
        "-a", "--algorithm",
        default="sha256",
        help=f"Hashing algorithm (default: sha256). Supported: {', '.join(sorted(SUPPORTED_ALGOS))}"
    )

    parser.add_argument(
        "-o", "--output",
        help="Optional: Save results to a JSON file"
    )

    args = parser.parse_args()

    try:
        logging.info(f"Hashing file: {args.file}")
        logging.info(f"Using algorithm: {args.algorithm}")

        result = hash_file(args.file, args.algorithm)

        output_data = {
            "file": os.path.abspath(args.file),
            "algorithm": args.algorithm,
            "hash": result,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        print("\n=== Hash Result ===")
        print(json.dumps(output_data, indent=4))

        if args.output:
            save_output(args.output, output_data)

    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
