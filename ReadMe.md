# COPA ATA LLM Project

This project is designed to assign ATA (Air Transport Association) codes to aircraft faults using a Language Learning Model (LLM) from HuggingFace. The project processes fault data and returns corresponding ATA codes based on the fault descriptions provided.

## Repository Structure

```plaintext
.
├── ATA-info.txt          # Contains detailed information about ATA codes.
├── copa-ata              # Directory containing the main code.
│   ├── main.py           # Main script to run the COPA ATA LLM.
│   └── __pycache__       # Compiled Python files.
├── faults.csv            # CSV file containing fault data.
├── filtered_csv.py       # Script to filter and process the CSV files.
├── poetry.lock           # Dependency lock file.
├── pyproject.toml        # Configuration file for project dependencies.
├── ReadMe.md             # This README file.
├── run.sh                # Shell script to execute the main program.
```

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- [Poetry](https://python-poetry.org/) for dependency management
- HuggingFace and other dependencies listed in `pyproject.toml`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/anand-kamble/copa-prompt-formatting
    cd copa-ata
    ```

2. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

### Running the Program

To execute the main script, simply run:

```bash
bash run.sh
```

This will invoke the Language Learning Model (LLM) to process fault data from `faults.csv` and assign ATA codes accordingly.

### Script Details

- **[main.py](copa-ata/main.py)**: The primary script that loads examples from `faults.csv`, reads ATA information from `ATA-info.txt`, and processes the data using a HuggingFace model. The script formats prompts and invokes the LLM for processing.

- **[filtered_csv.py](filtered_csv.py)**: This script filters and processes the original fault data from an external CSV file. It selects relevant columns (`FAULT_NAME`, `FAULT_SDESC`, and `ATA`) and saves them into `faults.csv`. This script should be run first if you need to generate or update the `faults.csv` file.

- **[run.sh](run.sh)**: A simple shell script that sets the source directory and entry file, then executes the `main.py` script.

### Configuration

- **[pyproject.toml](pyproject.toml)**: Contains the project’s configuration, including dependencies.
- **[poetry.lock](poetry.lock)**: Ensures consistent dependency management across environments.

### Data Files

- **[faults.csv](faults.csv)**: CSV file containing fault descriptions that need to be processed. This file is generated using the `filtered_csv.py` script.
- **[ATA-info.txt](ATA-info.txt)**: Provides detailed information about ATA codes, which is used by the `main.py` script to format prompts for the LLM.

## Usage Example

An example prompt processed by the LLM is:

```plaintext
Fault: BIRD STRIKE, DURING WALK AROUND BIRD STRIKE WAS NOTICED ON SIDE OF THE FUSELAGE
Expected ATA Code: ATA-XX
```

The LLM will respond with an ATA code based on the provided fault description.

