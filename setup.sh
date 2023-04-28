#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip not found. Installing pip..."
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py --user
    rm get-pip.py
else
    echo "pip already installed."
fi

# Check if required libraries are installed
if pip list | grep -q "googletrans\|pandas\|tqdm"
then
    echo "Required libraries already installed."
else
    # Install required libraries
    echo "Installing required libraries..."
    pip install --user googletrans pandas tqdm
fi

