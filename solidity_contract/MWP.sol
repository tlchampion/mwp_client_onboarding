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

  // The contract assumes the use of the OpenZeppelin SafeMath library for safe arithmetic operations.
  using SafeMath for uint;


  address payable private companyAccount;
  constructor() public {
    companyAccount = msg.sender;

  }

  mapping(address => Client) private clients;
  address[] private userIndex;


    event Deposit(address indexed userAddress, uint amount);
    event Withdrawal(address indexed userAddress, uint amount);
    event CompanyDeposit(address indexed userAddress, uint amount);
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

  /**
    * @dev Checks if the provided address is a registered user.
    * @param userAddress The address to check.
    * @return isIndeed True if the address is a registered user, false otherwise.
    */

  function isUser(address userAddress)
    public
    view
    returns(bool isIndeed)
  {
    if(userIndex.length == 0) return false;
    return (userIndex[clients[userAddress].index] == userAddress);
  }

  /**
    * @dev Inserts a new user into the system.
    * @param userAddress The address of the user to insert.
    * @param f_name The first name of the user.
    * @param l_name The last name of the user.
    * @param email The email address of the user.
    * @param portfolio The user's portfolio information.
    * @param balance The initial balance of the user.
    */

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

  /**
    * @dev Inserts or updates a user in the system.
    * @param f_name The first name of the user.
    * @param l_name The last name of the user.
    * @param email The email address of the user.
    * @param portfolio The user's portfolio information.
    */

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


  /**
    * @dev Retrieves the information of a user.
    * @param userAddress The address of the user to retrieve information for.
    * @return f_name The first name of the user.
    * @return l_name The last name of the user.
    * @return email The email address of the user.
    * @return portfolio The user's portfolio information.
    * @return balance The balance of the user.
    * @return index The index of the user in the userIndex array.
    */

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


  /**
    * @dev Updates the email address of a user.
    * @param userAddress The address of the user to update.
    * @param email The new email address.
    */

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

  /**
    * @dev Retrieves the total number of users.
    * @return count The total number of users.
    */

  function getUserCount()
    public
    view
    onlyCompany
    returns(uint count)
  {
    return userIndex.length;
  }

  /**
    * @dev Retrieves the user address at a specific index in the userIndex array.
    * @param index The index to retrieve the user address from.
    * @return userAddress The user address at the specified index.
    */

  function getUserAtIndex(uint index)
    public
    view
    onlyCompany
    returns(address userAddress)
  {
    return userIndex[index];
  }
    /**
    * @dev Sets the company account address.
    * @param _companyAccount The address of the company account.
    */
    function setCompanyAccount(address payable _companyAccount) public {
        companyAccount = _companyAccount;
    }
    /**
    * @dev Registers a client by adding them to the userIndex array and initializing their balance.
    * @param userAddress The address of the client to register.
    */
    function registerClient(address userAddress) public {
        require(!isUser(msg.sender), "Client is already registered");
        clients[userAddress].balance = 0;
        clients[userAddress].index     = userIndex.push(userAddress)-1;
        emit RegisterClient(
            userAddress,
            clients[userAddress].index,
            clients[userAddress].balance);
    }

    // TRANSACTIONS

    /**
    * @dev Client deposit function: Allows the client to deposit funds from their wallet into their reserve account.
    * It transfers money from their wallet to the contract wallet and increases their balance in the contract.
    */
    function userDeposit() public payable onlyClient {
        uint amount = msg.value;
        require(msg.sender.balance >= amount, "Not enough funds to deposit");

        clients[msg.sender].balance += amount;

        emit Deposit(msg.sender, amount);
         //The client's deposit is sent to the contract address
    }

    /**
    * @dev Retrieves the balance of a client.
    * @param userAddress The address of the client.
    * @return The balance of the client.
    */
    function getUserBalance(address userAddress) public view returns (uint) {
        return clients[userAddress].balance;
    }

    /**
    * @dev Retrieves the balance of the contract.
    * @return The balance of the contract.
    */
     function getContractBalance() public view returns (uint) {
      return address(this).balance;
    }

    /**
    * @dev Retrieves the balance of the company account.
    * @return The balance of the company account.
    */
    function getCompanyBalance() public view onlyCompany returns (uint) {
        return companyAccount.balance;
    }

    /**
    * @dev Client Withdraw Function: Allows the client to withdraw funds from their reserve account for use outside the investment platform.
    * It verifies that the client has a high enough balance (if not, they need to contact an advisor to sell assets), moves funds from the contract wallet to the client wallet, and reduces the client's balance.
    * @param _to The address to transfer the funds to.
    * @param amount The amount to withdraw.
    */
    function userWithdrawal(address payable _to, uint amount) public onlyClient {
        require(clients[msg.sender].balance >= amount, "Not enough funds in your reserve account to withdraw. Contact your advisor.");

        _to.transfer(amount);

        clients[_to].balance -= amount;
        emit Withdrawal(_to, amount);
    }

    /**
    * @dev Company Withdraw Function: Allows the company to withdraw from a client's reserve account to use for the purchase of portfolio assets.
    * It verifies that the company has a high enough balance (i.e., contract balance) and that the client has a high enough balance. If not, no withdraw can happen until client deposits more funds.
    * If the conditions are met, it moves funds from the contract wallet to the company wallet and reduces the client's balance.
    * @param _from The address of the client to withdraw funds from.
    * @param amount The amount to withdraw.
    */
    function companyWithdrawal(address _from, uint amount) public onlyCompany {
        require(address(this).balance >= amount, "Not enough funds in contract to withdraw.");
        require(clients[_from].balance >= amount, "Not enough funds in client fund to withdraw.");
        clients[_from].balance -= amount;
        companyAccount.transfer(amount);
        emit CompanyWithdrawal(_from, amount);
    }

    /**
    * @dev Company Deposit Function: Allows the company to deposit funds into the client's reserve account.
    * It verifies that the company has a high enough balance (i.e., contract balance).
    * If the condition is met, it moves funds from the company wallet to the client wallet and increases the client's balance.
    * @param _to The address of the client to deposit funds to.
    * @param amount The amount to deposit.
    */
    function companyDeposit(address _to) public payable onlyCompany {

        clients[_to].balance += msg.value;

        emit CompanyDeposit(_to, msg.value);
    }


}
