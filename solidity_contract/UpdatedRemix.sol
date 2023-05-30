pragma solidity ^0.5.17;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract MWP {

    struct Client {
     string f_name;
     string l_name;
     string email;
     string portfolio;
     uint balance;
     uint index;
  }
  
  using SafeMath for uint;

  address payable private companyAccount;
  constructor() public {
    companyAccount = msg.sender;
  }

  mapping(address => Client) private clients;
  address[] private userIndex;
	

	event Deposit(address indexed userAddress, uint amount);
	event Withdrawal(address indexed userAddress, uint amount);
	event CompanyDeposit(uint amount);
	event CompanyWithdrawal(uint amount);
	event RegisterClient(address indexed userAddress, uint index, uint balance);
	event LogNewUser(address indexed userAddress, uint index, string f_name, string l_name, string email, string portfolio, uint balance);
  event LogUpdateUser(address indexed userAddress, uint index, string f_name, string l_name, string email, string portfolio, uint balance);

	modifier onlyCompany() {
	    require(msg.sender == companyAccount, "Only Admin can access this function");
	    _;
	}

	modifier onlyClient() {
	   // require(clients[msg.sender].isRegistered, "Only registered clients can access this function");
	   require(isUser(msg.sender), "Only registered clients can access this function");
	    _;
	}


  function isUser(address userAddress)
    public 
    view
    returns(bool isIndeed) 
  {
    if(userIndex.length == 0) return false;
    return (userIndex[clients[userAddress].index] == userAddress);
  }

  function insertUser(
    address userAddress, 
    string memory f_name,
    string memory l_name, 
    string memory email,
    string memory portfolio,
    uint balance) public onlyCompany
    
  {

    require(!isUser(userAddress), "Already exists as a user");

    clients[userAddress].f_name = f_name; 
    clients[userAddress].l_name = l_name;
    clients[userAddress].email   = email;
    clients[userAddress].portfolio   = portfolio;
    clients[userAddress].balance = 0;
    clients[userAddress].index     = userIndex.push(userAddress).sub(1);
    emit LogNewUser(
        userAddress, 
        clients[userAddress].index, 
        f_name,
        l_name,
        email,
        portfolio,
        balance); 
      
    
  }
  
    function insertUpdateUser (
        
        string memory f_name,
        string memory l_name,
        string memory email,
        string memory portfolio) public
        
        {
        address userAddress = msg.sender;
        uint balance = 0;

        if(!isUser(userAddress)) {
            clients[userAddress].f_name = f_name; 
            clients[userAddress].l_name = l_name;
            clients[userAddress].email   = email;
            clients[userAddress].portfolio   = portfolio;
            clients[userAddress].balance = 0;
            clients[userAddress].index     = userIndex.push(userAddress).sub(1);
            emit LogNewUser(
                userAddress, 
                clients[userAddress].index, 
                f_name,
                l_name,
                email,
                portfolio,
                balance); 
      
    

        } else {
            
            clients[userAddress].f_name = f_name; 
            clients[userAddress].l_name = l_name;
            clients[userAddress].email   = email;
            clients[userAddress].portfolio   = portfolio;
           
            emit LogUpdateUser(
                userAddress, 
                clients[userAddress].index, 
                f_name,
                l_name,
                email,
                portfolio,
                clients[userAddress].balance); 
      
    


        }
    }



  function getUser(address userAddress)
    public 
    view
    returns(string memory f_name, string memory l_name, string memory email, string memory portfolio,uint balance, uint index)
  {
    require(isUser(userAddress), "Not a current user"); 
    return(
      clients[userAddress].f_name,
      clients[userAddress].l_name,
      clients[userAddress].email, 
      clients[userAddress].portfolio,
      clients[userAddress].balance, 
      clients[userAddress].index);
  } 
  
  function updateUserEmail(address userAddress, string memory email) 
    public
  {
    require(isUser(userAddress), "Not a current user"); 
    clients[userAddress].email = email;
    emit LogUpdateUser(
      userAddress, 
      clients[userAddress].index,
      clients[userAddress].f_name,
      clients[userAddress].l_name,
      email, 
      clients[userAddress].portfolio,
      clients[userAddress].balance);
   
  }
  

  function getUserCount() 
    public
    view
    onlyCompany
    returns(uint count)
  {
    return userIndex.length;
  }

  function getUserAtIndex(uint index)
    public
    view
    onlyCompany
    returns(address userAddress)
  {
    return userIndex[index];
  }

    function setCompanyAccount(address payable _companyAccount) public {
        companyAccount = _companyAccount;
    }

    function registerClient(address userAddress) public {
        require(!isUser(msg.sender), "Client is already registered");
        clients[userAddress].balance = 0; 
        clients[userAddress].index     = userIndex.push(userAddress).sub(1);
        emit RegisterClient(
            userAddress, 
            clients[userAddress].index, 
            clients[userAddress].balance); 
    }

    // TRANSACTIONS

    // Client deposit function: This function has the client deposit from their wallet iinto their reserve account
    // It transfers money from their wallet to the contract wallet and increases their balance in the contract
    function userDeposit(address userAddress, uint amount) public payable onlyClient {
        require(clients[userAddress].balance >= amount, "Not enough funds to deposit");
        clients[userAddress].balance = clients[userAddress].balance.sub(amount);
        clients[address(this)].balance = clients[address(this)].balance.add(amount);
        emit Deposit(userAddress, amount);
    }

    // Get client's balance
    function getUserBalance(address userAddress) public view returns (uint) {
        return clients[userAddress].balance;
    }

    // Get contract's balance
     function getContractBalance() public view returns (uint) {
      return address(this).balance;
    }

    // Get company's balance
    function getCompanyBalance() public view onlyCompany returns (uint) {
        return companyAccount.balance;
    }

    // Client Withdraw Function: This function has a client withdraw funds from their reserve account for use outside the investment platform. 
    // It does: verify the client has a high enough balance (if not, they need to contact an advisor to sell assets), move funds from contract wallet 
    // to client wallet and reduce client balance.

    function userWithdrawal(address userAddress, uint amount) public payable onlyClient {
        require(clients[address(this)].balance >= amount, "Not enough funds in your contract to withdraw. Contact your advisor.");
        clients[address(this)].balance = clients[address(this)].balance.sub(amount);
        clients[userAddress].balance = clients[userAddress].balance.add(amount);
        emit Withdrawal(userAddress, amount);
    }

    // Company Withdraw Function: This function has the company withdraw from a client's reserve account to use for purchase of portfolio assets
    // It does: verify company has high enough balance (i.e. contract balance) and that client has high enough balance - if not no withdraw can 
    // happen until client deposits more funds - move funds from contract wallet to company wallet - reduce balance of applicable client
    function companyWithdrawal(uint amount) public payable onlyCompany {
        require(clients[address(this)].balance >= amount, "Not enough funds to deposit for investment.");
        clients[companyAccount].balance = clients[companyAccount].balance.add(amount);
        clients[address(this)].balance = clients[address(this)].balance.sub(amount);
        emit CompanyWithdrawal(amount);
    }

    // Company Deposit Function: TThis function has the company deposit funds into a client's reserve account, such as after selling portfolio assets. 
    // It does: transfer money from company wallet to the contract wallet (company specific deposit function), increase the applicable client's balance in the contract.
    function companyDeposit(uint amount) public payable onlyCompany {
        require(clients[companyAccount].balance >= amount, "Not enough funds to return to the Client.");
        clients[companyAccount].balance = clients[companyAccount].balance.sub(amount); 
        clients[address(this)].balance = clients[address(this)].balance.add(amount);
        emit CompanyDeposit(amount);
        
    }


}


//Solidity