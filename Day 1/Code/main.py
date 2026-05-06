from algosdk.v2client import algod

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""

client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

status = client.status()

print("Connected to Algorand TestNet!")
print("Last Round:", status["last-round"])