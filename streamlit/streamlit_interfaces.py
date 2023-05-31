import streamlit as st
from web3 import Web3
from dotenv import load_dotenv
import os
from pathlib import Path
import json

load_dotenv()

def convert_to_eth(wei):
    return wei/1000000000000000000

# Ganache connection settings
# ganache_url = "HTTP://127.0.0.1:7545"
ganache_url = os.getenv("WEB3_PROVIDER_URI")
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Contract address and ABI
# contract_address = "0x1702BeFEeEA2E8a78f4Bef619056F71686B884d2"
contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
company_account = os.getenv("COMPANY_ADDRESS")
# contract_abi
with open(Path("./abi.json")) as file:
    contract_abi = json.load(file)

# Contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
accounts = web3.eth.accounts








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
        "Select Client Account", options=accounts)
    if st.button("Sign-in"):
        if contract.functions.isUser(account_address).call({'from': account_address}) == True:
            st.success("You are signed in!")
            # Display the balance on the Streamlit page
            client_balance = contract.functions.getUserBalance(account_address).call({'from': account_address})
            st.info(f"Your Balance is: {client_balance:,} Wei ({convert_to_eth(client_balance):.4f} ETH)")
        else:
            st.warning("No Account Found.")


    st.divider()

    st.markdown("### Deposit or Withdrawal of funds :moneybag:")

    amount = int(st.number_input("Amount (in Wei)"))

    # Client transfering funds to their account
    if st.button("Deposit"):
        if contract.functions.isUser(account_address).call({'from': account_address}) == True:
            try:
                contract.functions.userDeposit().transact(
                {'from': account_address, 'value': amount})
                client_balance = contract.functions.getUserBalance(
                account_address).call({'from': account_address})
                st.success(
                f"Deposit successful! Your New Balance is: {client_balance:,} Wei ({convert_to_eth(client_balance):.4f} ETH)")
            except:
                st.warning("Unable to process deposit. Please verify that your wallet has enough funds")
        else:
            st.warning("Only registered clients may make a deposit")


    # Client requesting withdrawing funds from their account
    if st.button("Withdraw"):
        if contract.functions.isUser(account_address).call({'from': account_address}) == True:
            try:
                contract.functions.userWithdrawal(account_address, amount).transact(
                {'from': account_address})
                client_balance = contract.functions.getUserBalance(
                account_address).call({'from': account_address})
                st.success(
                f"Successful Withdrawal! Your New Balance is: {client_balance:,} Wei ({convert_to_eth(client_balance):.4f} ETH)")
            except:
                st.error("Not enough funds in your reserve account to cover the requested withdraw amount. Contact your advisor.")
        else:
            st.warning("Only registered clients may withdraw funds")

# client viewing their current balance
    if st.button("View Balance"):
        if contract.functions.isUser(account_address).call({'from': account_address}) == True:
            client_balance = contract.functions.getUserBalance(
            account_address).call({'from': account_address})
            st.success(
            f"Your Balance is: {client_balance:,} Wei ({convert_to_eth(client_balance):.4f} ETH)")
        else:
            st.warning("Only registered clients have a balance")


else:

    subheader_style_admin = "<h2 style='color: #abdbd9;'>Admin Portal</h2>"
    st.markdown(subheader_style_admin, unsafe_allow_html=True)

    # Company account information
    st.markdown("### Company Account :rocket:")
    # company_account = contract.functions.companyAccount().call()
    st.write("Company Account:", company_account)
    # accounts = web3.eth.accounts
    # company_account = st.selectbox("Company Account Address", options=accounts[:1])

    if st.button("Check Company Wallet Balance"):
        company_balance = contract.functions.getCompanyBalance().call(
            {'from': company_account})
        st.info(f"Company Balance: {company_balance:,} Wei ({convert_to_eth(company_balance):.4f} ETH)")

    if st.button("Check Contract Balance"):
        contract_balance = contract.functions.getContractBalance().call(
        {'from': company_account})
        st.info(f"Contract Balance: {contract_balance:,} Wei ({convert_to_eth(contract_balance):.4f} ETH)")

    st.divider()

    st.markdown("### Sending or Withdrawal of funds :moneybag:")
    company_amount = int(st.number_input("Amount (in Wei)"))
    client_address = st.selectbox(
        "Select Client Account", options=accounts)

    # Display Client Data
    if st.button("Display Client Data"):
        if contract.functions.isUser(client_address).call({'from': company_account}) == True:
            info = contract.functions.getUser(
            client_address).call({'from': company_account})
            f_name = info[0]
            l_name = info[1]
            email = info[2]
            portfolio = info[3]
            balance = info[4]



            st.write("First Name:", f_name)
            st.write("Last Name:", l_name)
            st.write("Email:", email)
            st.write("Portfolio:", portfolio)
            st.write(f"Balance: {balance} Wei ({convert_to_eth(balance):.4f} ETH))")

        else:
            st.warning("Not a current client")

    # Send Money to Client
    if st.button("Deposit Funds To Client Account"):
        if contract.functions.isUser(client_address).call({'from': company_account}) == True:
            if contract.functions.getCompanyBalance().call(
            {'from': company_account}) >= company_amount:
                contract.functions.companyDeposit(client_address).transact(
                    {'from': company_account, 'value': company_amount})
                st.success("Money sent to client!")
                # Check Company Balance
                company_balance = contract.functions.getCompanyBalance().call(
                    {'from': company_account})
                contract_balance = contract.functions.getContractBalance().call({'from': company_account})
                client_balance = contract.functions.getUser(client_address).call({'from': company_account})[4]
                st.success(f"The remaining company Balance is: {company_balance:,} Wei ({convert_to_eth(company_balance):.4f} ETH)")
                st.success(f"The current contract balance is {contract_balance:,} Wei ({convert_to_eth(contract_balance):.4f} ETH)")
                st.success(f"The client's balance is {client_balance:,} Wei ({convert_to_eth(client_balance):.4f} ETH)\n")
            else:
                st.error("Not enough funds in company wallet to cover deposit amount requested.")
        else:
            st.warning("Not a current client. Unable to deposit funds")

    # Withdraw Money from Client
    if st.button("Withdraw Funds From Client Account"):
        if contract.functions.isUser(client_address).call({'from': company_account}) == True:
            if contract.functions.getUser(client_address).call({'from': company_account})[4] >= company_amount:
                contract.functions.companyWithdrawal(client_address,company_amount).transact({'from': company_account})
                st.success("Money received from client's account!")
                # Check Company Balance
                company_balance = contract.functions.getCompanyBalance().call(
                    {'from': company_account})
                contract_balance = contract.functions.getContractBalance().call({'from': company_account})
                client_balance = contract.functions.getUser(client_address).call({'from': company_account})[4]
                st.success(f"The new company balance is: {company_balance:,} Wei ({convert_to_eth(company_balance):.4f} ETH)")
                st.success(f"The current contract balance is {contract_balance:,} Wei ({convert_to_eth(contract_balance):.4f} ETH)")
                st.success(f"The client's balance is {client_balance:,} Wei ({convert_to_eth(client_balance):.4f} ETH)\n")
            else:
                st.error("Not enough funds in client account to cover requested withdrawal")
        else:
            st.warning("Not a current client. Unable to withdraw funds")

    st.divider()

# add a new client
    st.markdown("### Add Client Info")

    c_address = st.text_input("Client Public Address")
    c_lname = st.text_input("Client First Name")
    c_fname = st.text_input("Client Last Name")
    c_email = st.text_input("Client Email Address")
    c_portfolio = st.text_input("Client Desired Portfolio")

    if st.button("Add/Update Client"):
        if contract.functions.isUser(c_address).call({'from': company_account}) == True:
            st.warning("Client already exists. If needing to update user name and/or email address please use 'Update Client' instead")
        else:
            contract.functions.insertUser(c_address, c_lname, c_fname, c_email, c_portfolio, 0).transact({"from": company_account})
            st.success("Client Added")

# update an existing client
    if st.button("Update Client"):
        if contract.functions.isUser(c_address).call({'from': company_account}) == False:
            st.warning("Client does not exist. Please use 'Client Add' to add a new client.")
        else:
            contract.functions.updateUser(c_address, c_lname, c_fname, c_email, c_portfolio).transact({"from": company_account})
            st.success("Client Info Updated")


