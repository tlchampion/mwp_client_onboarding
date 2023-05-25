pragma solidity ^0.5.17;

contract MWP {

    struct Client {
     string f_name;
     string l_name;
     string email;
     string portfolio;
     uint balance;
     uint index;
  }
  
  address payable private companyAccount;
  constructor() public {
    companyAccount = msg.sender;
  }

  mapping(address => Client) private clients;
  address[] private userIndex;


    event Deposit(address indexed userAddress, uint amount);
    event Withdrawal(address indexed userAddress, uint amount);
    event WithdrawalRequest(address indexed userAddress, uint amount);
    event CompanyWithdrawal(address indexed userAddress, uint amount);
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
    clients[userAddress].index     = userIndex.push(userAddress)-1;
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
            clients[userAddress].index     = userIndex.push(userAddress)-1;
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
        clients[userAddress].index     = userIndex.push(userAddress)-1;
        emit RegisterClient(
            userAddress, 
            clients[userAddress].index, 
            clients[userAddress].balance); 
    }

    function getUserBalance(address userAddress) public view returns (uint) {
        return clients[userAddress].balance;
    }


    function getClientBalance(address _userAddress) public view onlyCompany returns (uint) {
        return clients[_userAddress].balance;
    }

    function getCompanyBalance() public view onlyCompany returns (uint) {
        return companyAccount.balance;
    }

    function getContractBalance() public view onlyCompany returns (uint) {
      return address(this).balance;
    }



    function deposit() public payable onlyClient {
        uint amount = msg.value;
        require(msg.sender.balance >= amount, "Not enough funds to deposit");
      
        clients[msg.sender].balance += amount;
     
        emit Deposit(msg.sender, amount);
        companyAccount.transfer(amount); //The client's deposit is sent to the Company account
    }

    function requestWithdrawal(uint _amount) public onlyClient {
        require(clients[msg.sender].balance >= _amount, "Insufficient balance");
        clients[msg.sender].balance -= _amount;
        emit WithdrawalRequest(msg.sender, _amount); //For withdrawal, the client sends a request that has to be approved by the company
    }


    function sendMoneyToClient(address payable _userAddress, uint _amount) public onlyCompany {
        require(_amount <= companyAccount.balance, "Insufficient balance");
        _userAddress.transfer(_amount);
        emit CompanyWithdrawal(_userAddress, _amount);
    }

}