[![Feature Validation](https://github.com/ZahraaNouri/2508_DS5111_vkx7ss/actions/workflows/validations.yml/badge.svg)](https://github.com/ZahraaNouri/2508_DS5111_vkx7ss/actions/workflows/validations.yml)

# VM Bootstrap & Development Environment Setup

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)
![GitHub](https://img.shields.io/badge/version--control-git-orange)

This repository contains automation scripts and configuration files to quickly bootstrap a new VM and set up a reproducible Python development environment.

**Goal:** make onboarding simple and fault-tolerant for new Data Scientists.

---

## 📌 Prerequisites

Before starting, ensure:

- You have a new VM instance running (AWS, Azure, GCP, or local).
- Git and SSH keys are configured on the VM so you can clone/push without typing credentials.
- You know the GitHub repository URL to clone.

**Clone the repo (if you haven't):**

```bash
# replace <your-username> and <repo> with your values
git clone git@github.com:<your-username>/<repo>.git
cd <repo>
```

---

## ⚙️ Setup Instructions

> All commands below assume you're in the repository root (the folder you cloned).

### 1. Initialize the VM

Run the bootstrap script that updates the system and installs essential tools:

```bash
bash scripts/init.sh
```

Example `scripts/init.sh` (what it should do at minimum):

```bash
#!/usr/bin/env bash

sudo apt update                          # bring package lists up to date
sudo apt install make -y                 # install `make` for automation
sudo apt install python3.12-venv -y      # python virtualenv support
sudo apt install tree -y                 # helpful file tree utility
```

**Test:**

```bash
tree
```

You should see a directory listing (not an error).

---

### 2. Configure GitHub Credentials

Set your Git identity so commits are tagged correctly. Edit `scripts/init_git_creds.sh` and replace the placeholders.

Example `scripts/init_git_creds.sh`:

```bash
#!/usr/bin/env bash

USER="your-email@example.com"
NAME="your-github-username"

git config --global user.email "${USER}"
git config --global user.name "${NAME}"
git config --global --list
```

Make the script executable and run it:

```bash
chmod +x scripts/init_git_creds.sh
bash scripts/init_git_creds.sh
```

**Test:**

```bash
git config --global --list
```

You should see `user.email` and `user.name`.

---

### 3. Create & Update Python Virtual Environment (Makefile)

A `Makefile` automates creating a virtual environment and installing dependencies.

Example `Makefile` (place at repo root):

```makefile
default:
	@cat Makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt
```

Create a `requirements.txt` in the repo root, e.g.:

```
pandas
numpy
```

Run:

```bash
make update
```

This will:

- create `env/` if missing (`python3 -m venv env`)
- activate the venv and upgrade pip
- install packages from `requirements.txt`

**Test:**

```bash
source env/bin/activate
pip list
```

You should see packages listed from `requirements.txt` (e.g., `pandas`, `numpy`).

---

## 📂 Repository Structure

```
repo-root/
│
├── scripts/
│   ├── init.sh              # VM initialization script
│   ├── init_git_creds.sh    # GitHub credentials setup
│
├── Makefile                 # Automates environment setup (targets: env, update)
├── requirements.txt         # Python dependencies (e.g., pandas, numpy)
└── README.md                # This file
```

---



