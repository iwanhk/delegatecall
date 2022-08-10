from scripts.functions import *

def code64(a):
    code= hex(a)[2:]
    return '0'*(64-len(code))+ code

def main():
    active_network = network.show_active()
    print("Current Network:" + active_network)

    admin, creator, consumer, iwan = get_accounts(active_network)

    try:
        if active_network in LOCAL_NETWORKS:
            test= TestContract.deploy(addr(admin))
            v = 123
            a = 10000
            # encoded_signature = test.getData(v, a)
            # print(encoded_signature)
            sig = Web3.keccak(text="callMe(uint256,uint256)")[:4].hex()
            data = sig+code64(v)+code64(a)
            # print(data)
            # assert encoded_signature == data
            proxy= Proxy.deploy(addr(admin))
            tx= proxy.makeCall(test, data)
            tx.wait(1)
            tx.return_value

            web3_f = web3.eth.contract(address=test.address, abi=test.abi)
            transaction= web3_f.functions.callMe(123,1).buildTransaction() # 获得函数调用的transaction

            tx= proxy.makeCall(transaction['to'], transaction['data'])
            tx.wait(1)
            tx.return_value

        if active_network in TEST_NETWORKS:
            test= TestContract.deploy(addr(admin))
            v = 123
            a = 10000
            encoded_signature = t.getData(v, a)
            print(encoded_signature)
            sig = Web3.keccak(text="callMe(uint256,uint256)")[:4].hex()
            v_hex = convert.to_bytes(v).hex()
            a_hex = convert.to_bytes(a).hex()
            data = sig+v_hex+a_hex
            print(data)
            assert encoded_signature == data

    except Exception:
        console.print_exception()
        # Test net contract address


if __name__ == "__main__":
    main()
