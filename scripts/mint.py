from scripts.functions import *


def main():
    active_network = network.show_active()
    print("Current Network:" + active_network)

    admin, creator, consumer, iwan = get_accounts(active_network)

    try:
        if active_network in LOCAL_NETWORKS:
            asset = Asset.deploy(addr(admin))
            con = DerivativeTree.deploy(
                asset, "MIT", "MIT TERMS", 0, "http://isotop/top/source/", addr(admin))

            asset.mint(0, addr(creator))
            asset.mint(1, addr(iwan))

            con.sign(0, addr(creator))
            con.sign(1, addr(iwan))

        if active_network in TEST_NETWORKS:
            nft = DerivativeTree[-1]
            asset = Asset[-1]

            asset.mint(0, addr(creator))
            asset.mint(1, addr(iwan))

            con.sign(0, addr(creator))
            con.sign(1, addr(iwan))

        if active_network in REAL_NETWORKS:
            nft = DerivativeTree[-1]
            asset = Asset[-1]

            asset.mint(0, addr(creator))
            asset.mint(1, addr(iwan))

            con.sign(0, addr(creator))
            con.sign(1, addr(iwan))

    except Exception:
        console.print_exception()
        # Test net contract address


if __name__ == "__main__":
    main()
