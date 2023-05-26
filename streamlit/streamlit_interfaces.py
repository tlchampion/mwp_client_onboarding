import streamlit as st
from web3 import Web3

# Ganache connection settings
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Contract address and ABI
contract_address = "0x1702BeFEeEA2E8a78f4Bef619056F71686B884d2"
contract_abi = [
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_to",
                                "type": "address"
            }
        ],
        "name": "companyDeposit",
        "outputs": [],
        "payable": True,
                "stateMutability": "payable",
                "type": "function"
    },
    {
        "inputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "CompanyDeposit",
        "type": "event"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_from",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "companyWithdrawal",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "CompanyWithdrawal",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "Deposit",
        "type": "event"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "string",
                "name": "f_name",
                                "type": "string"
            },
            {
                "internalType": "string",
                "name": "l_name",
                                "type": "string"
            },
            {
                "internalType": "string",
                "name": "email",
                                "type": "string"
            },
            {
                "internalType": "string",
                "name": "portfolio",
                                "type": "string"
            }
        ],
        "name": "insertUpdateUser",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "internalType": "string",
                "name": "f_name",
                                "type": "string"
            },
            {
                "internalType": "string",
                "name": "l_name",
                                "type": "string"
            },
            {
                "internalType": "string",
                "name": "email",
                                "type": "string"
            },
            {
                "internalType": "string",
                "name": "portfolio",
                                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                                "type": "uint256"
            }
        ],
        "name": "insertUser",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "index",
                                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "f_name",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "l_name",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "email",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "portfolio",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "balance",
                                "type": "uint256"
            }
        ],
        "name": "LogNewUser",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "index",
                                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "f_name",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "l_name",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "email",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "portfolio",
                                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "balance",
                                "type": "uint256"
            }
        ],
        "name": "LogUpdateUser",
        "type": "event"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            }
        ],
        "name": "registerClient",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "index",
                                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "balance",
                                "type": "uint256"
            }
        ],
        "name": "RegisterClient",
        "type": "event"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address payable",
                "name": "_companyAccount",
                                "type": "address"
            }
        ],
        "name": "setCompanyAccount",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "internalType": "string",
                "name": "email",
                                "type": "string"
            }
        ],
        "name": "updateUserEmail",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "userDeposit",
                "outputs": [],
                "payable": True,
                "stateMutability": "payable",
                "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address payable",
                "name": "_to",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "userWithdrawal",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "Withdrawal",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getCompanyBalance",
                "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getContractBalance",
                "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            }
        ],
        "name": "getUser",
        "outputs": [
            {
                "internalType": "string",
                "name": "f_name",
                        "type": "string"
            },
            {
                "internalType": "string",
                "name": "l_name",
                        "type": "string"
            },
            {
                "internalType": "string",
                "name": "email",
                        "type": "string"
            },
            {
                "internalType": "string",
                "name": "portfolio",
                        "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                        "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "index",
                        "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index",
                                "type": "uint256"
            }
        ],
        "name": "getUserAtIndex",
        "outputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                        "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            }
        ],
        "name": "getUserBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                        "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getUserCount",
                "outputs": [
            {
                "internalType": "uint256",
                "name": "count",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                                "type": "address"
            }
        ],
        "name": "isUser",
        "outputs": [
            {
                "internalType": "bool",
                "name": "isIndeed",
                        "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

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
