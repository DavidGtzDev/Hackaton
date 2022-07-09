pragma solidity >= 0.8.11;

contract HelloWorld {

    string public payload;

   function setPayload(string memory content) public {
        payload = content;
    }
    function sayHello() public pure returns (string memory) {
        return 'Hello World!';
    }
}