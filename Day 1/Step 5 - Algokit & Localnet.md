# Algorand Lock-In — Day 1 Step 5

### 06/05/2026

# Topic: AlgoKit + LocalNet Mental Model

## Core Transition

This step marks the transition from:

```text
using blockchain
```

to:

```text
running blockchain infrastructure locally
```

---

# What Is AlgoKit?

AlgoKit is NOT the blockchain SDK itself.

Correct mental model:

```text
Algorand SDK = low-level blockchain interaction library
AlgoKit = developer workflow + tooling framework
```

---

# Purpose Of AlgoKit

AlgoKit simplifies:

* project setup
* local blockchain management
* smart contract deployment
* testing workflows
* development tooling

Without AlgoKit, developers would manually configure:

* nodes
* blockchain services
* testing environments
* deployment workflows

---

# Ecosystem Analogy

| Ecosystem | Tool           |
| --------- | -------------- |
| React     | Vite / Next.js |
| Python    | Poetry         |
| Docker    | Docker Compose |
| Flutter   | Flutter CLI    |
| Algorand  | AlgoKit        |

---

# LocalNet

## Definition

LocalNet = a private blockchain network running locally on the developer's computer.

Mental model:

```text
LocalNet = private practice blockchain
```

---

# Why LocalNet Exists

Used for:

* development
* testing
* debugging
* experimentation
* smart contract iteration

Benefits:

* fast execution
* instant resets
* controlled environment
* no dependency on public TestNet

---

# Network Types

| Network  | Purpose                     |
| -------- | --------------------------- |
| MainNet  | Real production blockchain  |
| TestNet  | Public developer blockchain |
| LocalNet | Personal/private blockchain |

---

# Important Infrastructure Concept

Blockchain nodes are simply machines running blockchain software.

Using Docker, these services can run locally.

This means:

```text
local computer → hosts blockchain infrastructure
```

---

# What Runs Inside LocalNet?

When LocalNet starts, Docker launches containers for:

* Algorand node
* blockchain APIs
* local accounts
* supporting services

This creates a fully functional local blockchain ecosystem.

---

# Important Realization

Blockchain development is heavily related to:

* distributed systems
* backend engineering
* infrastructure
* APIs
* networking

It is NOT just “crypto programming.”

---

# Infrastructure Ownership Distinction

## Using AlgoNode/TestNet

```text
Developer uses someone else's infrastructure
```

---

## Using LocalNet

```text
Developer controls and runs infrastructure locally
```

This distinction becomes extremely important in professional blockchain development.

---

# LocalNet Commands

## Start LocalNet

```bash
algokit localnet start
```

Purpose:

* launch local blockchain services
* start Docker containers
* initialize local development environment

---

## Check LocalNet Status

```bash
algokit localnet status
```

Used to verify:

* running services
* container status
* blockchain environment health

---

# Docker Connection

This step reinforces why Docker matters.

Docker allows developers to:

* package infrastructure
* run isolated services
* simulate distributed systems locally

LocalNet internally relies on Docker containers.

---

# Step 5 Outcome

Completed:

* Understood AlgoKit purpose
* Understood LocalNet concept
* Understood local blockchain infrastructure
* Understood Docker's role in blockchain development
* Understood infrastructure ownership differences
* Learned how local blockchain networks are started and managed


---------------------------
---------------------------
---------------------------
---------------------------


# Additional Notes — SDK vs AlgoKit + Nodes & APIs

# SDK vs AlgoKit

## Algorand SDK

The Algorand SDK helps applications interact with blockchain infrastructure.

Purpose:

* interact with node APIs
* construct transactions
* query blockchain data
* sign transactions
* interact with smart contracts

Mental model:

```text
SDK = programming interface for blockchain interaction
```

Without the SDK, developers would manually:

* make HTTP requests
* serialize transactions
* encode blockchain data
* handle cryptographic formats

The SDK abstracts this complexity.

---

## AlgoKit

AlgoKit is a development toolkit/framework for Algorand developers.

Purpose:

* local blockchain setup
* project templates
* deployment workflows
* testing utilities
* development tooling
* improved developer experience

Mental model:

```text
AlgoKit = blockchain development toolkit/framework
```

---

# Best Comparison

| Layer   | Equivalent                                        |
| ------- | ------------------------------------------------- |
| SDK     | requests library / Firebase SDK / Supabase client |
| AlgoKit | Next.js CLI / Flutter CLI / Docker Compose        |

---

# Important Distinction

```text
SDK → helps applications TALK TO blockchain

AlgoKit → helps developers BUILD blockchain applications efficiently
```

---

# Nodes + APIs

# What Is A Node?

A node is simply:

```text
A computer running blockchain software
```

---

# Responsibilities Of A Node

Nodes:

* store blockchain data
* validate transactions
* sync with network
* participate in consensus
* expose APIs

---

# Important Realization

Nodes themselves expose APIs.

Meaning:

```text
Node software
    ├── blockchain logic
    ├── validation
    ├── networking
    └── API server
```

So the same machine:

* participates in blockchain
* stores blockchain state
* exposes APIs for developers/apps

---

# Mental Model

Similar to a database server:

```text
PostgreSQL server
    ├── stores database
    ├── processes queries
    └── exposes connection interface
```

Similarly:

```text
Blockchain node
    ├── stores blockchain
    ├── validates transactions
    └── exposes APIs
```

---

# Example

When Python code calls:

```python
client.status()
```

The application is basically asking:

```text
"Hey node, give me current blockchain status."
```

The node responds through its exposed API.

---

# What Is AlgoNode?

AlgoNode is an infrastructure provider.

Purpose:

* run Algorand nodes professionally
* expose public node APIs
* provide infrastructure access for developers

Instead of running personal node infrastructure, developers can use AlgoNode endpoints.

---

# Current Architecture

```text
Your Python App
        ↓
Algorand SDK
        ↓
AlgoNode API endpoint
        ↓
AlgoNode node machine
        ↓
Algorand blockchain network
```

---

# Why Multiple Nodes Exist

Blockchain systems are decentralized.

If only one node existed:

* system becomes centralized
* easier to manipulate
* single point of failure

Instead:
many nodes:

* replicate blockchain state
* validate transactions
* agree on network state
* maintain decentralization

---

# Final Important Insight

Blockchain development is heavily related to:

* APIs
* infrastructure
* networking
* distributed systems
* backend engineering

This is why cloud, Docker, networking, and backend knowledge are extremely valuable in Web3 development.
