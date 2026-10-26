stock = int(input("Stock: "))

requested = int(input("Requested quantity: "))

# if requested < stock:
#     print("Order can be fulfilled")
# else:
#     print("Insufficient stock")



def check_stock(stock, requested):
    """Siparişin mevcut stokla karşılanıp karşılanamayacağını kontrol eder.

    Args:
        stock (int): Depodaki ürün adedi.
        requested (int): Müşterinin istediği adet.

    Returns:
        bool: Stok yeterliyse True, değilse False.
    """
    return requested <= stock

print("Order can be fulfilled:", check_stock(stock, requested))