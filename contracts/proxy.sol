// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

contract Proxy {
    function makeCall(address realOne, bytes memory arg) external returns(bool success, bytes memory data){
        return realOne.delegatecall(arg);
    }
}