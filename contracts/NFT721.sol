// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract TestContract {
    event Log(bytes code, uint256 i, uint256 j);
    event Log1(string func, uint256 i, uint256 j);

    uint256 public i;
    function callMe(uint256 j, uint256 a) public returns (uint256) {
        emit Log1("TestContract.callMe(%d,%d) called", j, a);
        i += j;
        return i;
    }
    function getData(uint256 j, uint256 a) external pure returns (bytes memory) {
        // emit Log1("call signature encoded:", j, a);
        // emit Log(abi.encodeWithSignature("callMe(uint256,uint256)"), j, a);
        return abi.encodeWithSignature("callMe(uint256,uint256)", j, a);
    }
}

contract NFT721 is ERC721Enumerable {
    using Strings for uint256;
    string public baseUIR;
    constructor(string memory _base) ERC721("NFT721", "NFT721") {
        baseUIR= _base;
    }

    function mint(address to, uint256 tokenId) external {
        _mint(to, tokenId);
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return baseUIR;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "nonexistent token");

        string memory baseURI = _baseURI();
        return string(abi.encodePacked(baseURI, tokenId.toString(), ".json"));
    }
}
