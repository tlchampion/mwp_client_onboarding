import questionary
import sys
import re

with open('../solidity_contract/abi.txt', 'r') as abiText:
    abiData = abiText.read()

abiData_caps = re.sub(r"true", "True", abiData)
abiData_caps = re.sub(r"false", "False", abiData_caps)

abiData_lower = re.sub(r"True", "true", abiData)
abiData_lower = re.sub(r"False", "false", abiData_lower)

web3Address = "http://127.0.0.1:7545"
panelURL = "http://localhost:9501"
streamlitURL = "http://localhost:8501"
contractAddr = questionary.text("What is the contract address?").ask()

Web3Check = questionary.confirm("Is your Web3 Provider (i.e. Ganache) running at http://127.0.0.1:7545 ?").ask()
if Web3Check == False:
    web3Address = questionary.text("What is the URL to your Web3 Provider (i.e. Ganache)?").ask()


with open("../streamlit/.env","w") as envFile:
    envFile.write(f"""SMART_CONTRACT_ADDRESS = "{contractAddr}"\nWEB3_PROVIDER_URI = "{web3Address}" """)

with open("../streamlit/abi.json","w") as abi:
    abi.write(f"{abiData_lower}")

with open("../react/.env", "w") as env:
    env.write("GENERATE_SOURCEMAP=false")

with open("../react/src/imports/abi.js", "w") as abi:
    abi.write(f"export const contractABI = {abiData_lower}")

with open("../react/src/imports/contract.js","w") as contract:
    contract.write(f'export const contractAddr = "{contractAddr}"')

with open("../react/src/imports/streamlit.js", "w") as streamlit:
    streamlit.write(f'export const streamlitURL = "{streamlitURL}"')

with open("../react/src/imports/panel.js", "w") as panel:
    panel.write(f'export const panelURL = "{panelURL}"')
