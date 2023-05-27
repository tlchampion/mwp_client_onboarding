import streamlit as st
from web3 import Web3
from dotenv import load_dotenv
import os
from pathlib import Path
import json

load_dotenv()


# Ganache connection settings
# ganache_url = "HTTP://127.0.0.1:7545"
ganache_url = os.getenv("WEB3_PROVIDER_URI")
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Contract address and ABI
# contract_address = "0x1702BeFEeEA2E8a78f4Bef619056F71686B884d2"
contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
# contract_abi
with open(Path("./abi.json")) as file:
    contract_abi = json.load(file)

# Contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
accounts = web3.eth.accounts
company_account = accounts[0]
# Streamlit app
header_style = "<h1 style='color: #88ccc9;'>Investment Platform &#x1F4C8;</h1>"
st.markdown(header_style, unsafe_allow_html=True)

portal = st.sidebar.radio("Select Portal", ("Client Portal", "Admin Portal"))


if portal == "Client Portal":

    subheader_style = "<h2 style='color: #abdbd9;'>Client Portal</h2>"
    st.markdown(subheader_style, unsafe_allow_html=True)

    # Client sign-in and balance check
    st.markdown("### Client Sign-in :rocket:")

    account_address = st.selectbox(
        "Select Client Account", options=accounts[1:])
    if st.button("Sign-in"):
        contract.functions.isUser(account_address).call(
            {'from': account_address})
        st.success("You are signed in!")
        # Display the balance on the Streamlit page
        client_balance = contract.functions.getUserBalance(
            account_address).call({'from': account_address})
        st.info(f"Your Balance is: {client_balance}")

    st.markdown("### Deposit or Withdrawal of funds :moneybag:")

    amount = int(st.number_input("Amount"))

    # Client transfering funds to their account
    if st.button("Deposit"):
        contract.functions.userDeposit().transact(
            {'from': account_address, 'value': amount})
        client_balance = contract.functions.getUserBalance(
            account_address).call({'from': account_address})
        st.success(
            f"Deposit successful! Your New Balance is: {client_balance}")

    # Client requesting withrawing funds from their account
    if st.button("Withdraw"):
        contract.functions.userWithdrawal(account_address, amount).transact(
            {'from': account_address, 'value': amount})
        client_balance = contract.functions.getUserBalance(
            account_address).call({'from': account_address})
        st.success(
            f"Successful Withdrawal! Your New Balance is: {client_balance}")

else:

    subheader_style_admin = "<h2 style='color: #abdbd9;'>Admin Portal</h2>"
    st.markdown(subheader_style_admin, unsafe_allow_html=True)

    # Company account information
    st.markdown("### Company Account :rocket:")
    # company_account = contract.functions.companyAccount().call()
    st.write("Company Account:", company_account)
    # accounts = web3.eth.accounts
    # company_account = st.selectbox("Company Account Address", options=accounts[:1])

    if st.button("Check Company Account"):
        company_balance = contract.functions.getCompanyBalance().call(
            {'from': company_account})
        st.info(f"Company Balance: {company_balance}")

    st.markdown("### Sending or Withdrawal of funds :moneybag:")
    company_amount = int(st.number_input("Amount"))
    client_address = st.selectbox(
        "Select Client Account", options=accounts[1:])

    # Display Client Data
    if st.button("Display Client Data"):
        f_name = contract.functions.getUser(
            client_address).call({'from': client_address})[0]
        l_name = contract.functions.getUser(
            client_address).call({'from': client_address})[1]
        email = contract.functions.getUser(
            client_address).call({'from': client_address})[2]
        portfolio = contract.functions.getUser(
            client_address).call({'from': client_address})[3]

        st.write("First Name:", f_name)
        st.write("Last Name:", l_name)
        st.write("Email:", email)
        st.write("Portfolio:", portfolio)

    # Send Money to Client
    if st.button("Send Money to Client"):
        contract.functions.companyDeposit(company_amount).transact(
            {'from': company_account, 'value': company_amount})
        st.success("Money sent to client!")
        # Check Company Balance
        company_balance = contract.functions.getCompanyBalance().call(
            {'from': company_account})
        st.success(f"The remaining company Balance is: {company_balance}")

    # Withdraw Money from Client
    if st.button("Withdraw Money from Client"):
        contract.functions.companyWithdrawal(
            company_amount).transact({'value': company_amount})
        st.success("Money received from client's contract!")
        # Check Company Balance
        contract_balance = contract.functions.getContractBalance().call()
        st.success(
            f"The resulting balance in the client's contract is: {company_balance}")
