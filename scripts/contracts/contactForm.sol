pragma solidity ^0.5.17;

contract ContactForm {

    struct UserStruct {
     string f_name;
     string l_name;
     string email;
     string portfolio;
     uint index;
  }
  
  mapping(address => UserStruct) private userStructs;
  address[] private userIndex;

  event LogNewUser   (address indexed userAddress, uint index, string f_name, string l_name, string email, string portfolio);
  event LogUpdateUser(address indexed userAddress, uint index, string f_name, string l_name, string email, string portfolio);
  function isUser(address userAddress)
    public 
    view
    returns(bool isIndeed) 
  {
    if(userIndex.length == 0) return false;
    return (userIndex[userStructs[userAddress].index] == userAddress);
  }

  function insertUser(
    address userAddress, 
    string memory f_name,
    string memory l_name, 
    string memory email,
    string memory portfolio) public
    
  {

    require(!isUser(userAddress), "Already exists as a user");
    userStructs[userAddress].f_name = f_name; 
    userStructs[userAddress].l_name = l_name;
    userStructs[userAddress].email   = email;
    userStructs[userAddress].portfolio   = portfolio;
    userStructs[userAddress].index     = userIndex.push(userAddress)-1;
    emit LogNewUser(
        userAddress, 
        userStructs[userAddress].index, 
        f_name,
        l_name,
        email,
        portfolio); 
      
    
  }
  
    function insertUpdateUser (
        
        string memory f_name,
        string memory l_name,
        string memory email,
        string memory portfolio) public
        
        {
        address userAddress = msg.sender;
        if(!isUser(userAddress)) {
            userStructs[userAddress].f_name = f_name; 
            userStructs[userAddress].l_name = l_name;
            userStructs[userAddress].email   = email;
            userStructs[userAddress].portfolio   = portfolio;
            userStructs[userAddress].index     = userIndex.push(userAddress)-1;
            emit LogNewUser(
                userAddress, 
                userStructs[userAddress].index, 
                f_name,
                l_name,
                email,
                portfolio); 
      
    

        } else {
            userStructs[userAddress].f_name = f_name; 
            userStructs[userAddress].l_name = l_name;
            userStructs[userAddress].email   = email;
            userStructs[userAddress].portfolio   = portfolio;
            
            emit LogUpdateUser(
                userAddress, 
                userStructs[userAddress].index, 
                f_name,
                l_name,
                email,
                portfolio); 
      
    


        }
    }



  function getUser(address userAddress)
    public 
    view
    returns(string memory f_name, string memory l_name, string memory email, string memory portfolio, uint index)
  {
    require(isUser(userAddress), "Not a current user"); 
    return(
      userStructs[userAddress].f_name,
      userStructs[userAddress].l_name,
      userStructs[userAddress].email, 
      userStructs[userAddress].portfolio, 
      userStructs[userAddress].index);
  } 
  
  function updateUserEmail(address userAddress, string memory email) 
    public
     
  {
    require(isUser(userAddress), "Not a current user"); 
    userStructs[userAddress].email = email;
    emit LogUpdateUser(
      userAddress, 
      userStructs[userAddress].index,
      userStructs[userAddress].f_name,
      userStructs[userAddress].l_name,
      email, 
      userStructs[userAddress].portfolio);
   
  }
  

  function getUserCount() 
    public
    view
    returns(uint count)
  {
    return userIndex.length;
  }

  function getUserAtIndex(uint index)
    public
    view
    returns(address userAddress)
  {
    return userIndex[index];
  }

}