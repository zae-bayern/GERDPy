#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install it to run GERDPy."
    exit 1
fi

# Run the guiman.py script
python3 guiman.py
