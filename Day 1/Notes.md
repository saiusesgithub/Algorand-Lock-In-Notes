# Algorand Lock-In — Day 1 (May 6)

Today is NOT a “build huge dApp” day.

Today is:

# friction-removal day

If Day 1 is smooth, the entire month becomes easier.

Your objective today:

> “I can successfully interact with Algorand locally without confusion.”

That’s it.

---

# TODAY’S GOALS

By end of today, you should have:

* AlgoKit installed
* local environment working
* wallet created
* TestNet account funded
* first transaction done
* basic understanding of Algorand architecture
* first tiny script interacting with blockchain

No smart contracts yet.

---

# TODAY’S STRUCTURE

## PART 1 — Understand the Ecosystem (30–45 mins)

You are NOT deeply studying blockchain today.

Only understand:

---

## Concepts To Learn

### 1. What is a blockchain?

Focus on:

* distributed ledger
* blocks
* transactions
* immutable history

NOT:

* Byzantine fault tolerance
* cryptography math
* consensus papers

---

### 2. Wallets

Understand:

* public address
* private key
* mnemonic phrase
* signing transactions

VERY important concept.

---

### 3. TestNet vs MainNet

Understand:

* fake money
* development/testing
* why developers use testnet

---

### 4. Smart Contracts

Only high-level:

* code on blockchain
* state storage
* rules execution

No deep internals yet.

---

## Resource

ONLY:
Alchemy University Intro to Blockchain

Use it like:

> “remove confusion”

NOT:

> “finish entire course today”

---

# PART 2 — Environment Setup (MAIN TASK)

This is the real Day 1.

---

# Install These

## REQUIRED

### 1. Docker Desktop

Needed because AlgoKit uses containers heavily.

---

### 2. Git

---

### 3. VS Code

Extensions:

* Python
* Docker
* GitHub Copilot (optional)

---

### 4. AlgoKit

Official setup only.

You’ll verify installation using terminal.

---

# PART 3 — Wallet Setup

Install:

# Pera Wallet

Create:

* TestNet wallet

IMPORTANT:
Save mnemonic safely.

Understand:

* wallet address
* signing
* accounts

---

# PART 4 — First Blockchain Interaction

This is where things become real.

You’ll:

* fund wallet from faucet
* send a transaction
* see transaction explorer
* observe confirmations

This single step removes LOTS of blockchain fear/confusion.

---

# PART 5 — First Python Interaction

You’ll create:

* tiny Python script
* connect to Algorand TestNet
* fetch account info
* print balance

This is your:

# “hello world”

for Algorand.

---

# OUTPUT OF TODAY

By tonight you should have:

✅ working AlgoKit
✅ Docker working
✅ wallet setup
✅ testnet ALGO
✅ first transaction
✅ first Python blockchain script

That is MORE than enough for Day 1.

---

# WHAT WE ARE DOING TOMORROW (Day 2)

Tomorrow is where development actually starts.

---

# DAY 2 PREVIEW (May 7)

## Main Focus:

# AlgoKit + local development workflow

You’ll learn:

* how Algorand projects are structured
* how AlgoKit creates projects
* localnet
* app structure
* how contracts are organized
* how Python smart contracts work

---

## First Actual Build

Tiny:

# Counter Contract

Features:

* increment counter
* store value on chain
* read state

This becomes your:

* first smart contract
* first blockchain state interaction

---

# IMPORTANT

Do NOT rush into frontend yet.

Backend/blockchain mental model first.

If you skip this:
wallet integration later becomes painful.

---

# YOUR DAY 1 EXECUTION ORDER

Follow EXACTLY this order:

1. Install Docker
2. Install AlgoKit
3. Verify AlgoKit works
4. Install/create Pera wallet
5. Get TestNet ALGO
6. Send one transaction
7. Write tiny Python balance-fetch script
8. Read light blockchain fundamentals

That’s it.

---

# TODAY’S MENTAL RULE

Do NOT optimize.
Do NOT compare ecosystems.
Do NOT watch random “Top 10 Web3 frameworks” videos.

Your ONLY job:

# make the environment work

Once done:
reply with:

* what worked
* what broke
* screenshots/errors if stuck
* how much time you still have today

Then I’ll decide whether to:

* stop Day 1 there
  OR
* pull part of Day 2 into today.
------

Perfect — that actually makes this MUCH better for consistency.

Then this lock-in becomes:

> Learn by building + guided explanation in one place.

No switching tabs constantly.
No tutorial hopping.
No “wait this YouTuber explained differently.”
No getting lost in documentation hell.

I’ll act like:

* mentor
* roadmap
* debugger
* concept explainer
* project reviewer

And the docs become:

> backup reference only when needed.

That’s honestly the best setup for your learning style.

---

# Then Let’s Redefine Day 1 Properly

Today will be:

# “Understanding what a blockchain ACTUALLY is while setting up your environment.”

Not separate theory + setup.

We’ll mix:

* concepts
* practicals
* mental models
* tiny execution steps

exactly together.

---

# DAY 1 — REAL PLAN

# SECTION 1 — What Are We Even Building Toward?

Before tools:
you need the mental model.

---

# Traditional Apps vs Blockchain Apps

Normal app:

Frontend → Backend → Database

Example:
Instagram:

* React frontend
* Python/Java backend
* PostgreSQL/MySQL DB

The company controls everything.

---

# Blockchain App (dApp)

Frontend → Smart Contract → Blockchain

Instead of:

* backend logic
* centralized database

you put:

* rules
* state
* transactions

on-chain.

---

# Example

Traditional voting app:

* server stores votes
* admin can manipulate DB

Blockchain voting app:

* smart contract stores votes
* rules are public
* harder to tamper with
* every transaction is recorded

That’s the BIG idea.

Not crypto.
Not coins.
Not hype.

It’s:

# trust through shared state + public execution

---

# SECTION 2 — Core Blockchain Concepts

These are the ONLY concepts you need today.

---

# 1. Wallet

A wallet is NOT where coins are stored.

This is a VERY important correction.

Coins are stored:

# on the blockchain.

Wallet stores:

* private key
* public key
* ability to sign transactions

Think:
wallet = identity + authorization.

---

# 2. Public Address

Like:
account username.

Safe to share.

Example:
`ABCD123...`

People send ALGO to this.

---

# 3. Private Key / Mnemonic

This is:

# your ownership proof.

If someone has it:
they own the wallet.

Mnemonic phrase:

* human-readable backup
* generates private key

Never expose this.

---

# 4. Transaction

A transaction is:

# a signed state change request.

Examples:

* send ALGO
* call smart contract
* vote
* store data

---

# 5. Blockchain

Blockchain is basically:

# a distributed append-only ledger.

Every node:

* stores history
* verifies transactions
* agrees on state

---

# 6. Smart Contract

A smart contract is:

# backend logic running on-chain.

Instead of:

```python
if voted:
    reject()
```

on your own server,

the blockchain executes it.

That’s why it becomes trustable/public.

---

# SECTION 3 — Why Algorand Specifically?

You already made a VERY good choice for your situation.

Why Algorand fits YOU:

---

## Python Support

Huge advantage.

Ethereum world:

* Solidity
* JS ecosystem
* harder onboarding

Algorand:

* Python smart contracts
* cleaner tooling
* easier mental overhead

---

## Low Friction

You want:

* execution
* projects
* consistency

not:

* ecosystem wars

Algorand is excellent for that.

---

## Fast + Cheap TestNet

Makes experimentation painless.

---

# SECTION 4 — Understanding the Architecture

SUPER important.

Your future voting app will roughly look like:

```text
Frontend (React/Next)
        ↓
Wallet (Pera)
        ↓
Smart Contract (Python)
        ↓
Algorand Blockchain
```

---

# What Each Part Does

## Frontend

UI only.

Buttons:

* vote
* connect wallet
* show results

---

## Wallet

Signs transactions.

Equivalent of:
“yes, I authorize this.”

---

## Smart Contract

Contains rules.

Example:

* one vote per wallet
* candidate count
* result storage

---

## Blockchain

Stores:

* state
* transaction history
* contract data

---

# SECTION 5 — NOW We Setup

NOW the tools make sense.

Otherwise installation becomes meaningless.

---

# TODAY’S PRACTICAL TASKS

# TASK 1 — Install Docker Desktop

Why?

Because AlgoKit uses containers heavily.

You’ll later run:

* local blockchain network
* testing environments
* supporting services

inside Docker.

So Docker becomes your:

# “blockchain lab machine”

---

# TASK 2 — Install AlgoKit

AlgoKit is basically:

# the official developer toolkit for Algorand.

Equivalent to:

* starter framework
* CLI
* local tooling
* project generator

all combined.

---

# TASK 3 — Create Wallet

Install:

# Pera Wallet

You’ll:

* create TestNet wallet
* save mnemonic
* get address

---

# TASK 4 — Get TestNet ALGO

Important concept:

## MainNet

Real money.

## TestNet

Fake money for developers.

You’ll use:

# faucet

to get free ALGO.

This is where blockchain starts feeling real.

---

# TASK 5 — First Transaction

This matters psychologically.

Once you:

* send ALGO
* see confirmation
* inspect transaction explorer

blockchain suddenly stops feeling abstract.

---

# TASK 6 — First Python Interaction

Tiny script:

* connect to Algorand
* fetch balance
* print account info

This becomes your:

# first blockchain program

---

# WHAT TOMORROW WILL BE

If today goes well:

Tomorrow:

# first smart contract.

You’ll learn:

* what blockchain state actually means
* global/local state
* contract methods
* deployment flow

And build:

# Counter App

You press button →
value increments on-chain.

That’s where the magic starts.

---

# RIGHT NOW — START HERE

Tell me:

1. OS
2. Is Docker already installed?
3. Is Python already installed?
4. VS Code installed?
5. Git installed?

Then we start setup together step-by-step.
 

 ----


 GOOD.

You already removed 70% of beginner friction.

That means we can skip the boring setup phase and start actually understanding + interacting with Algorand today.

So today officially becomes:

# Day 1 = First Real Blockchain Interaction

Goal:

> “I understand how accounts + transactions + blockchain interaction actually work.”

---

# TODAY’S FLOW

We’ll do this in order:

1. Understand Algorand accounts properly
2. Connect to TestNet
3. Fund wallet
4. Send transaction
5. Understand transaction lifecycle
6. Write first Python blockchain script
7. Understand what AlgoKit actually does
8. (Optional stretch) Start localnet

---

# STEP 1 — Understand Accounts PROPERLY

This is EXTREMELY important.

Most beginners misunderstand this.

---

# Mental Model

Your wallet is NOT:

```text
wallet = money storage
```

Instead:

```text
wallet = key manager + signer
```

The blockchain stores:

* balances
* state
* transaction history

NOT the wallet app.

---

# What Pera Wallet Actually Does

Pera Wallet mainly:

* manages private keys
* shows balances
* signs transactions
* connects to dApps

That’s it.

---

# Important Architecture

```text
Blockchain = actual data/state

Wallet = permission + signing tool
```

---

# Why Signing Matters

Suppose someone tries:

```text
Send 100 ALGO from Srujan → Random Person
```

Blockchain asks:

# “prove you own this account.”

That proof is:

# cryptographic signature

generated using:

# private key

Wallet handles this for you.

---

# IMPORTANT CONCEPT

## Public Address

Safe to share.

Like:

```text
username/account number
```

---

## Private Key / Mnemonic

NEVER share.

Equivalent to:

```text
full ownership
```

If leaked:
account gone.

---

# STEP 2 — Create TestNet Account

Now practical.

Inside Pera:

* create/import account
* switch network to:

# TestNet

NOT MainNet.

---

# WHY TESTNET EXISTS

Blockchain development needs:

* experimentation
* testing
* debugging

without using real money.

So TestNet behaves almost like real blockchain:

* real transactions
* real confirmations
* real smart contracts

but:

# fake ALGO

---

# STEP 3 — Get TestNet ALGO

You’ll use:

# Algorand Faucet

This gives free TestNet ALGO.

Search:

```text
Algorand TestNet faucet
```

Paste your wallet address.

Get funds.

---

# IMPORTANT OBSERVATION

Notice:
you now officially have:

* blockchain account
* blockchain balance
* on-chain identity

without:

* bank
* signup
* centralized approval

That’s one of the BIG conceptual shifts in Web3.

---

# STEP 4 — FIRST TRANSACTION

After getting TestNet ALGO:

Send a tiny amount:

* either to another test account
  OR
* back to yourself

Even 0.001.

---

# WHY THIS MATTERS

You’ll observe:

* signing
* submission
* confirmation
* explorer tracking

This removes “magic feeling.”

---

# STEP 5 — Understand Transaction Lifecycle

SUPER important.

When you send ALGO:

---

# What Actually Happens

## 1. Transaction Created

Contains:

* sender
* receiver
* amount
* fee

---

## 2. Wallet Signs

Using:

# private key

---

## 3. Broadcast to Network

Transaction sent to Algorand nodes.

---

## 4. Validators Verify

Checks:

* signature valid?
* enough balance?
* correct format?

---

## 5. Included in Block

Blockchain state updates.

---

## 6. Confirmation

Transaction finalized.

---

# KEY INSIGHT

Blockchain is basically:

# distributed state transition.

Transactions change state.

That’s the core.

---

# STEP 6 — Your First Python Blockchain Script

NOW the fun starts.

We interact programmatically.

---

# What You’ll Learn Here

You’ll realize:

> blockchain is just another programmable system.

Not magic.

---

# Create Folder

```bash
mkdir algo-day1
cd algo-day1
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# Install SDK

```bash
pip install py-algorand-sdk
```

---

# NOW — Understanding the SDK

SDK = Software Development Kit.

This lets Python:

* talk to blockchain
* fetch account info
* send transactions
* interact with smart contracts

Equivalent to:

```text
backend API wrapper for blockchain
```

---

# Create `main.py`

Paste this:

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

# RUN IT

```bash
python main.py
```

---

# WHAT THIS ACTUALLY DID

Your Python app:

* connected to Algorand node
* requested blockchain status
* received latest block info

Meaning:

# your code just talked to a blockchain.

That’s your first real developer milestone.

---

# IMPORTANT CONCEPT

## Node

A blockchain node is basically:

# a machine running blockchain software.

Like:

```text
backend server for blockchain network
```

---

# Algonode

You are using:

# public RPC endpoint

Meaning:
you don’t need your own blockchain node yet.

Same concept as:

* using external API
* cloud database endpoint

---

# STEP 7 — Understand AlgoKit

VERY important.

Most beginners treat AlgoKit like magic.

Don’t.

---

# AlgoKit Is Basically:

## 1. Project Generator

Creates boilerplate.

---

## 2. Dev Environment Manager

Helps run local blockchain.

---

## 3. Deployment Tool

Deploy contracts/apps.

---

## 4. Workflow Simplifier

Removes repetitive setup pain.

---

# Mental Model

Think:

```text
Algorand SDK = low-level interaction

AlgoKit = developer framework/tooling layer
```

VERY similar to:

```text
Flask vs Python sockets
Next.js vs raw React setup
```

---

# OPTIONAL STRETCH GOAL (ONLY if energy remains)

Try:

```bash
algokit localnet start
```

This launches:

# your own local blockchain network.

This is HUGE conceptually.

You are literally running blockchain infra locally.

Tomorrow this becomes important.

---

# WHAT TOMORROW WILL BE

Tomorrow:

# smart contracts begin.

You’ll learn:

* blockchain state
* global/local storage
* app calls
* contract deployment

And build:

# Counter Contract

This is where:

> “oh wait… this is basically backend engineering on-chain”

starts clicking.

---

# YOUR TASK NOW

Do these:

1. Get TestNet ALGO
2. Send first transaction
3. Run Python script
4. Try localnet (optional)

Then report:

* what worked
* what confused you
* any errors
* whether you still have time/energy today

Then I’ll decide whether to pull tomorrow’s first contract intro into today.
