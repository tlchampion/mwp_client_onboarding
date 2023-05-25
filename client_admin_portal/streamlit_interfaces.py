import streamlit as st
from web3 import Web3

# Ganache connection settings
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Contract address and ABI
contract_address = "0xBEd06061D8F9505Dc800e4D1aAE1C8C7E9A9263F"
contract_abi = [
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address payable",
                "name": "_userAddress",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                                "type": "uint256"
            }
        ],
        "name": "approveWithdrawal",
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
        "constant": False,
        "inputs": [],
        "name": "deposit",
                "outputs": [],
                "payable": True,
                "stateMutability": "payable",
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
                "internalType": "uint256",
                "name": "_amount",
                                "type": "uint256"
            }
        ],
        "name": "requestWithdrawal",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address payable",
                "name": "_userAddress",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                                "type": "uint256"
            }
        ],
        "name": "sendMoneyToClient",
        "outputs": [],
        "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
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
        "name": "WithdrawalRequest",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "_userAddress",
                                "type": "address"
            }
        ],
        "name": "getClientBalance",
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
        "inputs": [],
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

# Streamlit app
st.title("Investment Platform")

portal = st.sidebar.radio("Select Portal", ("Client Portal", "Admin Portal"))
accounts = web3.eth.accounts
account_address = st.selectbox("Select Client Account", options=accounts[1:])
if portal == "Client Portal":
    st.subheader("Client Portal")

    # Client sign-in and balance check
   # account_address = st.text_input("Account Address")

    amount = int(st.number_input("Amount"))

    if st.button("Client Sign-in"):
        contract.functions.isUser(account_address).call(
            {'from': account_address})
        st.success("You are signed in!")
        client_balance = contract.functions.getUserBalance().call()
        st.info(f"Your Balance is: {client_balance}")

        # Client transfer of funds to the Company Account
    if st.button("Deposit funds"):

        contract.functions.deposit().transact(
            {'from': account_address, 'value': amount})
        st.success("Deposit successful!")

        # Client requesting funds withdrawal to the Company
    if st.button("Withdraw"):

        contract.functions.requestWithdrawal(
            amount).transact({'from': account_address})
        st.success("Withdrawal request sent to company!")

else:
    st.subheader("Admin Portal")

    # Company account information
    company_account = accounts[0]

    if st.button("Go to Company Account"):
        contract.functions.setCompanyAccount(company_account).transact()
        st.success("Company account set successfully!")

        company_balance = contract.functions.getCompanyBalance().call()
        st.info(f"Company Balance: {company_balance}")

    if st.button("Send Money to Client"):
        client_address = st.text_input("Client Address")
        amount = st.number_input("Amount")
        contract.functions.sendMoneyToClient(client_address, amount).transact()
        st.success("Money sent to client!")

    withdrawal_requests = st.button("View Withdrawal Requests")

    if withdrawal_requests:
        withdrawal_logs = web3.eth.getLogs({
            "fromBlock": 0,
            "toBlock": "latest",
            "address": contract_address,
            "topics": [web3.keccak(text="WithdrawalRequest(address,uint256)").hex()]
        })

        for log in withdrawal_logs:
            log_data = contract.events.WithdrawalRequest().processLog(log)
            client_address = log_data[0]['args']['clientAddress']
            withdrawal_amount = log_data[0]['args']['amount']
            approved = st.checkbox(
                f"Approve withdrawal of {withdrawal_amount} ETH for {client_address}")
            if approved:
                contract.functions.approveWithdrawal(
                    client_address, withdrawal_amount).transact()
                st.success(f"Withdrawal approved for {client_address}")
