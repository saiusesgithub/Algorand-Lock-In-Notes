# Algorand Lock-In — Day 3 Step 3

### 11/05/2026 (supposed to do on 8th , but stuff came up , so doing this in college on 11th as i have free time)

# Topic: App IDs + Contract Interaction

## Core Goal

Understand:

* what App IDs are
* why smart contracts need App IDs
* how frontend knows which contract to call
* how blockchain locates contracts
* where contracts are stored
* how nodes execute/verify smart contracts

---

# What Happens During Smart Contract Deployment?

When a smart contract is deployed:

```text
Blockchain creates application
        ↓
Assigns unique App ID
```

Example:

```text
App ID = 1024
```

This becomes:

```text
unique identifier of deployed blockchain application
```

---

# Important Mental Model

App IDs are similar to:

| System          | Identifier  |
| --------------- | ----------- |
| SQL Database    | Primary Key |
| YouTube         | Video ID    |
| Backend Service | Service URL |
| Blockchain App  | App ID      |

---

# Why Are App IDs Necessary?

Blockchain networks may contain:

* thousands
* millions

of deployed smart contracts.

Frontend must specify:

```text
Which smart contract should receive this transaction?
```

This is why App IDs exist.

---

# Example Voting App

Suppose voting contract has:

```text
App ID = 5001
```

Frontend transaction request becomes:

```text
Call:
vote("Alice")

on App ID:
5001
```

Meaning:

* blockchain knows which smart contract to execute
* correct app state gets modified

---

# Important Realization

Frontend does NOT simply say:

```text
hey blockchain vote pls
```

Frontend specifically targets:

```text
particular deployed smart contract app
```

using:

```text
App ID
```

---

# What Happens Internally?

When blockchain receives transaction:

* it checks App ID
* locates corresponding smart contract
* executes corresponding contract logic
* updates corresponding blockchain state

---

# Huge Realization

Deployment creates:

* smart contract application
* application state
* callable methods
* application identity

App ID becomes:

```text
permanent reference to deployed smart contract
```

---

# How Frontends Store App IDs

Usually stored in:

* config files
* constants
* environment variables
* backend configuration

Example:

```javascript
const APP_ID = 5001;
```

Then frontend uses this App ID for all blockchain interactions.

---

# Connection To Generated Clients

Generated files like:

```text
counter_client.py
```

internally use:

* App ID
* ABI/contract spec

for correct smart contract interaction.

---

# User Understanding (Refined)

Question:

```text
Why is App ID important when multiple apps exist?
```

Initial understanding:

```text
There are multiple App IDs,
so blockchain must know which app's smart contract to execute.
Different apps may perform different logic.
```

This understanding was fundamentally correct.

---

# What Happens If Wrong App ID Is Used?

Initial understanding:

```text
Vote may not be counted in correct app.
```

Correct.

More specifically:

* wrong smart contract executes
* wrong app state changes
* transaction may fail
* vote may go to wrong application
* frontend behavior becomes incorrect

---

# IMPORTANT DOUBT — Where Are Smart Contracts Stored?

Question:

```text
Where are smart contracts actually stored?
```

Answer:

```text
Smart contracts are stored on blockchain.
```

Meaning:

* blockchain stores deployed contract programs
* blockchain stores corresponding app state
* blockchain stores app metadata

---

# Are Smart Contracts Stored On Every Node?

YES.

Just like blockchain state replication:

```text
smart contract programs are replicated across nodes
```

Meaning:

* nodes maintain copies of contracts
* nodes maintain copies of blockchain state
* nodes can independently verify execution

---

# Do Nodes Execute Smart Contracts?

YES.

When transactions arrive:

* nodes execute smart contract logic
* nodes verify results
* nodes confirm deterministic execution

This is why:

```text
all nodes must agree on same result
```

---

# Important Realization

Blockchain does NOT work like:

```text
one special server executes contract
```

Instead:

```text
network collectively verifies execution
```

---

# Important Question

```text
How does blockchain know WHICH contract to execute?
```

Answer:

```text
Transaction contains App ID.
```

Blockchain uses App ID to:

* locate deployed contract
* execute corresponding contract logic

---

# Important Clarification

Frontend/node does NOT manually choose:

```text
which node should execute smart contract
```

Instead:

* transaction propagates through network
* nodes process transaction
* blockchain consensus verifies execution

This is distributed system behavior.

---

# Huge Mental Model

Blockchain behaves like:

```text
distributed replicated backend infrastructure
```

NOT:

```text
single backend server
```

---

# Major Conceptual Shift

Smart contracts stopped feeling like:

```text
magic programs floating somewhere
```

and started feeling like:

```text
deployed distributed backend applications identified by App IDs
```

---

# Step 3 Outcome

Completed:

* Understood App IDs
* Understood why App IDs are necessary
* Understood how frontend targets contracts
* Understood smart contract replication across nodes
* Understood node execution/verification flow
* Understood how blockchain locates contracts
* Understood distributed contract execution model
