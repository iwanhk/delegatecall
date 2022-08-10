from scripts.functions import *


def main():
    active_network = network.show_active()
    print("Current Network:" + active_network)

    admin, creator, consumer, iwan = get_accounts(active_network)

    try:
        test= TestContract.deploy(addr(admin))
        proxy= Proxy.deploy(addr(admin))
        flat_contract('TestContract', TestContract.get_verification_info())
        flat_contract('Proxy', Proxy.get_verification_info())

    except Exception:
        console.print_exception()
        # Test net contract address


if __name__ == "__main__":
    main()
