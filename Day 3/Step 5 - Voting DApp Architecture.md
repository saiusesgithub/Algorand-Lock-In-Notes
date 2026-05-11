# Algorand Lock-In — Day 3 Step 5

### 11/05/2026 (supposed to do on 8th , but stuff came up , so doing this in college on 11th as i have free time)

# Topic: Architecture Of A Real Voting dApp

## Core Goal

Connect all previously learned concepts into:

```text
one coherent buildable blockchain application architecture
```

This step combines:

* frontend
* wallet integration
* transactions
* signing
* smart contracts
* global/local state
* blockchain state fetching
* UI updates

into a single real-world system.

---

# Future Voting dApp

Planned simplified voting dApp features:

* connect wallet
* vote once
* show live vote counts
* show updated results

This architecture is sufficient for:

* hackathons
* MVPs
* learning projects
* prototypes
* portfolio applications

---

# Full High-Level Architecture

```text
Flutter/Web Frontend
        ↓
Pera Wallet Connection
        ↓
Transaction Signing
        ↓
Algorand Smart Contract
        ↓
Blockchain Global/Local State
        ↓
Frontend Fetches Updated State
        ↓
UI Updates
```

---

# 1. Frontend Layer

Possible technologies:

* Flutter
* React
* web frontend

Responsibilities:

* buttons
* screens
* wallet connection UI
* vote UI
* result display
* loading/error states

Mental model:

```text
Frontend = user experience layer
```

---

# Example Frontend UI

```text
[ Connect Wallet ]

Alice → 62 votes
Bob → 31 votes

[ Vote Alice ]
[ Vote Bob ]
```

Simple architecture is enough for MVP.

---

# 2. Wallet Integration Layer

Frontend connects to:

```text
Pera Wallet
```

Purpose:

* identify user
* retrieve wallet address
* request transaction approvals
* sign transactions

---

# Important Realization

Wallet acts as:

```text
blockchain login + authorization system
```

Instead of username/password:

```text
wallet address becomes user identity
```

---

# 3. Smart Contract Layer

Smart contract contains:

* voting rules
* validation logic
* state update logic

Example rules:

* one vote per wallet
* valid candidate only
* increment candidate count
* prevent duplicate voting

Mental model:

```text
Smart contract = backend business logic
```

---

# 4. Blockchain State Layer

Voting dApp requires BOTH:

* global state
* local state

---

# Global State

Shared application-wide state.

Example:

```text
Alice votes = 62
Bob votes = 31
```

Shared across all users.

---

# Local State

Wallet/account-specific state.

Example:

```text
Wallet XYZ:
already_voted = true
```

Different for each wallet.

---

# Huge Important Realization

Voting applications REQUIRE both:

* global state
* local state

This made the earlier global/local state concepts finally feel practical.

---

# Full Voting Flow

Suppose user clicks:

```text
Vote Alice
```

Flow:

```text
Frontend creates transaction request
        ↓
Calls vote("Alice") on App ID
        ↓
Wallet popup appears
        ↓
User approves/signs transaction
        ↓
Transaction sent to blockchain
        ↓
Smart contract checks:
    - already voted?
    - valid candidate?
        ↓
Global state updates:
    Alice += 1
        ↓
Local state updates:
    already_voted = true
        ↓
Frontend fetches latest state
        ↓
UI refreshes
```

---

# User Understanding (Refined)

Scenario:

```text
User already voted once and tries to vote again.
```

Initial understanding:

```text
User clicks vote button again.
Wallet signs transaction.
Smart contract checks rules.
Transaction fails.
UI shows transaction failed.
```

This understanding was fundamentally correct.

---

# Refined Duplicate Vote Flow

```text
User clicks Vote Alice again
        ↓
Frontend creates transaction request
        ↓
Wallet popup appears
        ↓
User signs transaction
        ↓
Transaction sent to blockchain
        ↓
Smart contract checks local state:
    already_voted = true
        ↓
Contract rejects transaction
        ↓
Blockchain state does NOT change
        ↓
Frontend receives failure/error
        ↓
UI displays vote failure message
```

---

# Important Realization

Wallet signing ONLY proves:

```text
wallet owner approved transaction
```

Signing does NOT automatically mean:

```text
transaction is valid
```

Smart contract rules still decide:

* accept
* reject

---

# IMPORTANT DOUBT — What If User Creates Multiple Wallets?

Question:

```text
What if user creates multiple Pera wallet accounts and votes multiple times?
```

This is an EXTREMELY important practical blockchain product-design question.

---

# Important Realization

Blockchain identity is fundamentally:

```text
wallet-based
```

NOT:

* human-based
* email-based
* Aadhaar-based

Meaning:

```text
one person can create multiple wallets
```

---

# Therefore

A simple:

```text
one vote per wallet
```

system does NOT guarantee:

```text
one vote per human
```

---

# This Is Called

```text
Sybil problem / Sybil attack
```

One user creates many identities/wallets.

---

# Real Projects Solve This Using

Possible approaches:

* KYC/identity verification
* college/student email verification
* NFT-based eligibility
* token ownership rules
* phone/email verification
* DAO membership systems
* reputation systems
* proof-of-personhood systems

---

# Example Practical Solution

College voting app:

```text
Only wallets linked to verified student IDs can vote.
```

---

# Huge Product Realization

Blockchain gives:

* wallet ownership
* transaction verification
* distributed trust

BUT:

```text
human identity verification is still a product/application problem
```

This is a HUGE real-world Web3 realization.

---

# Major Conceptual Shift

Blockchain applications stopped feeling like:

```text
isolated smart contracts
```

and started feeling like:

```text
full-stack distributed software systems
```

---

# Important Final Realization

Most practical blockchain development involves:

* frontend architecture
* wallet integration
* state management
* UX design
* identity design
* product logic
* SDK integration

NOT primarily:

* low-level VM engineering
* opcode writing
* compiler internals

---

# Step 5 Outcome

Completed:

* Connected frontend + wallet + contract + state architecture
* Understood real voting dApp architecture
* Understood duplicate-vote rejection flow
* Understood local/global state usage practically
* Understood why signing ≠ automatic validity
* Understood Sybil attack problem
* Understood identity challenges in Web3 systems
* Connected blockchain with full-stack product architecture
