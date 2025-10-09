#!/bin/bash

set -e  # Stop script on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Project Environment Setup ===${NC}\n"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 not found. Please install Python 3.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "Python found: ${GREEN}$PYTHON_VERSION${NC}"

if ! python3 -m venv --help &> /dev/null; then
    echo -e "${YELLOW}Installing python3-venv...${NC}"
    sudo apt update
    sudo apt install -y python3-venv
fi

VENV_DIR="venv"

if [ -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Existing virtual environment found. Removing...${NC}"
    rm -rf "$VENV_DIR"
fi

echo -e "\n${GREEN}Creating virtual environment...${NC}"
python3 -m venv "$VENV_DIR"

echo -e "${GREEN}Activating virtual environment...${NC}"
source "$VENV_DIR/bin/activate"

echo -e "\n${GREEN}Upgrading pip...${NC}"
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    echo -e "\n${GREEN}Installing dependencies from requirements.txt...${NC}"
    pip install -r requirements.txt
else
    echo -e "${RED}Warning: requirements.txt not found!${NC}"
fi

echo -e "\n${GREEN}=== Setup completed successfully! ===${NC}"
echo -e "\nTo activate the virtual environment in the future, run:"
echo -e "${YELLOW}source venv/bin/activate${NC}"
echo -e "\nTo deactivate the virtual environment:"
echo -e "${YELLOW}deactivate${NC}"
