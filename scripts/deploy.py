from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)


def deploy_fund_me():
    account = get_account()
    print(account.address)
    print(f"The active network is..  {network.show_active()}")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print(f"price feed address {price_feed_address}")
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        # publish_source=config["networks"][network.show_active()]["verify"],
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Conract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
