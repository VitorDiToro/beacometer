#!/bin/bash

set -e  # Stop script on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

VENV_NAME="ble"
PYTHON_VERSION="3.14.0"

echo -e "${GREEN}=== Project Environment Setup ===${NC}\n"

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if [ -d "$PYENV_ROOT" ]; then
    echo -e "${GREEN}pyenv already installed${NC}"
    eval "$(pyenv init -)"
else
    echo -e "${YELLOW}pyenv not found. Installing pyenv...${NC}"
    
    sudo apt update
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
        libffi-dev liblzma-dev
    
    curl https://pyenv.run | bash
    
    eval "$(pyenv init -)"
    
    echo -e "${GREEN}pyenv installed successfully!${NC}"
    echo -e "${YELLOW}Note: Add the following to your ~/.bashrc or ~/.zshrc:${NC}"
    echo -e 'export PYENV_ROOT="$HOME/.pyenv"'
    echo -e 'export PATH="$PYENV_ROOT/bin:$PATH"'
    echo -e 'eval "$(pyenv init -)"'
    echo ""
fi

if ! pyenv versions | grep -q "$PYTHON_VERSION"; then
    echo -e "\n${YELLOW}Installing Python $PYTHON_VERSION...${NC}"
    pyenv install "$PYTHON_VERSION"
else
    echo -e "${GREEN}Python $PYTHON_VERSION already installed${NC}"
fi

echo -e "\n${GREEN}Setting Python $PYTHON_VERSION for this project...${NC}"
pyenv local "$PYTHON_VERSION"

PYTHON_PATH=$(pyenv which python)
echo -e "Using Python: ${GREEN}$PYTHON_PATH${NC}"

if [ -d "$VENV_NAME" ]; then
    echo -e "${YELLOW}Existing virtual environment found. Removing...${NC}"
    rm -rf "$VENV_NAME"
fi

echo -e "\n${GREEN}Creating virtual environment...${NC}"
python -m venv "$VENV_NAME"

echo -e "${GREEN}Activating virtual environment...${NC}"
source "$VENV_NAME/bin/activate"

echo -e "\n${GREEN}Upgrading pip...${NC}"
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    echo -e "\n${GREEN}Installing dependencies from requirements.txt...${NC}"
    pip install -r requirements.txt
else
    echo -e "${RED}Warning: requirements.txt not found!${NC}"
fi

echo -e "\n${GREEN}=== Setup completed successfully! ===${NC}"
echo -e "\nPython version: ${GREEN}$(python --version)${NC}"
echo -e "\nTo activate the virtual environment in the future, run:"
echo -e "${YELLOW}source $VENV_NAME/bin/activate${NC}"
echo -e "\nTo deactivate the virtual environment:"
echo -e "${YELLOW}deactivate${NC}"