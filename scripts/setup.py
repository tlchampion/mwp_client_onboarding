import questionary
import sys

with open('../solidity_contract/abi.txt', 'r') as abiText:
    abiData = abiText.read()


# print(data)

# with open('abi_new.txt', 'w') as abiNew:
#     abiNew.write(data)

panelURL = "http://localhost:9501"
streamlitURL = "http://localhost:8501"
web3Address = "http://127.0.0.1:7545"
contractAddr = questionary.text("What is the contract address?").ask()
checkPanelURL = questionary.confirm("Is Panel running on the recommended port 9501").ask()
if checkPanelURL == False:
    panelURL = questionary.text("What is the full URL for the Panel Dashboard?").ask()
Web3Check = questionary.confirm("Is your Web3 Provider (i.e. Ganache) running at http://127.0.0.1:7545 ?").ask()
if Web3Check == False:
    web3Address = questionary.text("What is the URL to your Web3 Provider (i.e. Ganache)?").ask()
checkStreamlitURL = questionary.confirm("Is Streamlit running on the recommended port 8501?").ask()
if checkStreamlitURL == False:
    streamlitURL = questionary.text("What is the full URL for the Streamlit app?").ask()
abiCheck = questionary.confirm("Did you modify the Solidity contract file?").ask()
if abiCheck:
    updateABI = questionary.confirm("Did you copy the new ABI configuration to the abi.txt file in the root of the setup folder?").ask()
    if updateABI == False:
        print("Exiting setup. Please update the abi.txt file then rerun this script")
        sys.exit()


# write .env file for streamlit. Need to add in the contract address and the Web3 provider address
with open("../streamlit/.env","w") as envFile:
    envFile.write(f"""SMART_CONTRACT_ADDRESS = "{contractAddr}"\nWEB3_PROVIDER_URI = "{web3Address}" """)

# write files for use with react: contract address, ABI, streamlit url, panel url
with open("../react/src/imports/streamlit.js", "w") as streamlit:
    streamlit.write(f'export const streamlitURL = "{streamlitURL}"')

with open("../react/src/imports/panel.js", "w") as panel:
    panel.write(f'export const panelURL = "{panelURL}"')

with open("../react/src/imports/contract.js","w") as contract:
    contract.write(f'export const contractAddr = "{contractAddr}"')

with open("../react/src/imports/abi.js", "w") as abi:
    abi.write(f"export const contractABI = {abiData}")

with open("../react/.env", "w") as env:
    env.write("GENERATE_SOURCEMAP=false")
