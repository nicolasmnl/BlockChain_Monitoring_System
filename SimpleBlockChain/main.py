from datetime import datetime
from blocks.blockchain import Blockchain


def main():
    manufacturer = {
        'transactions':
            [
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 1,
                    'product_serial': 50001000,
                    'name': 'cotton pants',
                    'from': 'Manufacturer X',
                    'to': 'Transportation X',
                    'message': 'This product is in a good order',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002000,
                    'name': 'cotton shirt',
                    'from': 'Manufacturer X',
                    'to': 'Transportation X',
                    'message': 'This product is in a good order',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002001,
                    'name': 'cotton shirt',
                    'from': 'Manufacturer X',
                    'to': 'Transportation X',
                    'message': 'This product is in a good order',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                }
            ]
    }

    transportation = {
        'transactions':
            [
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 1,
                    'product_serial': 50001000,
                    'name': 'cotton pants',
                    'from': 'Transportation X',
                    'to': 'Retailer X',
                    'shipping_id': 100,
                    'message': 'This product is in a good order. Shipped',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002000,
                    'name': 'cotton shirt',
                    'from': 'Transportation X',
                    'to': 'Retailer X',
                    'shipping_id': 101,
                    'message': 'This product is in a good order. Shipped',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002001,
                    'name': 'cotton shirt',
                    'from': 'Transportation X',
                    'to': 'Retailer X',
                    'shipping_id': 102,
                    'message': 'Product damaged',
                    'digital_signature': 'retailer review',
                    'flagged': 'Y'
                }
            ]
    }

    retailer = {
        'transactions':
            [
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 1,
                    'product_serial': 50001000,
                    'name': 'cotton pants',
                    'from': 'Retailer X',
                    'to': 'Storage',
                    'receiving_id': 400,
                    'message': 'This product is in a good order. Received',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002000,
                    'name': 'cotton shirt',
                    'from': 'Retailer X',
                    'to': 'Storage',
                    'receiving_id': 400,
                    'message': 'This product is in a good order. Received',
                    'digital_signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002001,
                    'name': 'cotton shirt',
                    'from': 'Retailer X',
                    'to': 'RTV',
                    'receiving_id': 401,
                    'message': 'Box damaged',
                    'digital_signature': 'rejected',
                    'flagged': 'Y'
                }
            ]
    }

    blockchain = Blockchain()
    a = blockchain.add(manufacturer)
    b = blockchain.add(transportation)
    c = blockchain.add(retailer)
    print(blockchain.chain)
    blockchain.get_transactions('all')


if __name__ == '__main__':
    main()
