# Algorand Lock-In — Day 1 Step 4

### 06/05/2026

# Topic: First Python → Blockchain Interaction

## Goal

Understand how application code communicates with a blockchain network.

This step marks the transition from:

```text
Blockchain user → Blockchain developer
```

---

# Full Architecture

```text
Your Python Code
        ↓
Algorand SDK
        ↓
algod API
        ↓
Algorand Node
        ↓
Algorand Blockchain Network
```

---

# Layer-by-Layer Understanding

## 1. Python Application

The developer-written program.

Can later become:

* backend service
* automation script
* dApp backend
* smart contract interaction layer

---

## 2. Algorand SDK

SDK = Software Development Kit.

Purpose:

* simplify blockchain interaction
* abstract low-level API handling
* provide helper methods

Without SDK:

* manual HTTP requests would be needed
* transactions would require manual formatting/serialization

Mental model:

```text
SDK = helper library for blockchain interaction
```

---

## 3. algod API

The primary API exposed by Algorand nodes.

Used for:

* network status
* transaction submission
* account queries
* smart contract interaction

Important realization:

```text
Blockchain interaction happens through node APIs.
```

---

## 4. Node

A node is a machine running Algorand software.

Responsibilities:

* store blockchain state
* validate transactions
* sync with network
* expose APIs

---

## 5. Blockchain Network

The distributed system formed by many connected nodes.

Maintains:

* consensus
* state
* history

---

# AlgoNode Concept

AlgoNode is an infrastructure provider that hosts Algorand nodes and exposes public APIs.

Instead of running personal node infrastructure, developers can use hosted endpoints.

Example endpoint:

```python
https://testnet-api.algonode.cloud
```

Mental model:

```text
AlgoNode = hosted blockchain infrastructure provider
```

---

# Python Setup

## Project Folder

```bash
mkdir algo-day1
cd algo-day1
```

---

## Virtual Environment

```bash
python -m venv venv
```

Purpose:

* isolate project dependencies
* avoid global package conflicts

---

## Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

---

## Install Algorand SDK

```bash
pip install py-algorand-sdk
```

This allows Python to communicate with Algorand nodes.

---

# First Blockchain Interaction Script

```python
from algosdk.v2client import algod

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""

client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

status = client.status()

print("Connected to Algorand TestNet!")
print("Last Round:", status["last-round"])
```

---

# Code Breakdown

## Import

```python
from algosdk.v2client import algod
```

Imports the algod client used for blockchain interaction.

---

## Node Endpoint

```python
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
```

Defines the public node API endpoint.

---

## Client Creation

```python
client = algod.AlgodClient(...)
```

Creates a connection interface to blockchain infrastructure.

---

## Status Request

```python
client.status()
```

Requests blockchain network status.

Equivalent mental model:

```text
GET blockchain network state
```

---

# Important Realization

The Python app does NOT directly talk to “the blockchain.”

Instead:

```text
Python app → node API → blockchain network
```

This is similar to interacting with distributed backend infrastructure.

---

# Key Insight

Blockchain development is fundamentally:

* API interaction
* distributed systems
* cryptographic signing
* state management

This is why backend, cloud, and networking knowledge are highly relevant in Web3.

---

# Step 4 Outcome

Completed:

* Understood blockchain interaction architecture
* Understood nodes and node APIs
* Understood SDK role
* Setup Python environment
* Installed Algorand SDK
* Connected Python application to Algorand TestNet
* Queried live blockchain state
