def test_read_product(session):
    # Arrange: Create a product
    product = Product(name="Laptop", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act: Read the product from the database
    fetched_product = session.query(Product).filter_by(name="Laptop").first()

    # Assert: Check that the product was fetched correctly
    assert fetched_product.name == "Laptop"
def test_update_product(session):
    # Arrange: Create and add a product
    product = Product(name="Laptop", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act: Update the product's category
    product.category = "Computers"
    session.commit()

    # Assert: Check that the category is updated
    updated_product = session.query(Product).filter_by(name="Laptop").first()
    assert updated_product.category == "Computers"
def test_delete_product(session):
    # Arrange: Create and add a product
    product = Product(name="Laptop", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act: Delete the product
    session.delete(product)
    session.commit()

    # Assert: Ensure the product no longer exists
    deleted_product = session.query(Product).filter_by(name="Laptop").first()
    assert deleted_product is None
def test_list_all_products(session):
    # Arrange: Add multiple products
    session.add_all([
        Product(name="Laptop", category="Electronics", available=True),
        Product(name="Phone", category="Electronics", available=False)
    ])
    session.commit()

    # Act: List all products
    products = session.query(Product).all()

    # Assert: Check that all products are retrieved
    assert len(products) == 2
def test_find_by_name(session):
    # Arrange: Add a product
    product = Product(name="Laptop", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act: Find the product by name
    fetched_product = session.query(Product).filter_by(name="Laptop").first()

    # Assert: Check the name matches
    assert fetched_product.name == "Laptop"
def test_find_by_category(session):
    # Arrange: Add products with categories
    session.add_all([
        Product(name="Laptop", category="Electronics", available=True),
        Product(name="Table", category="Furniture", available=False)
    ])
    session.commit()

    # Act: Find products in the "Electronics" category
    electronics = session.query(Product).filter_by(category="Electronics").all()

    # Assert: Ensure only electronics are retrieved
    assert len(electronics) == 1
    assert electronics[0].name == "Laptop"
def test_find_by_availability(session):
    # Arrange: Add products with different availability
    session.add_all([
        Product(name="Laptop", category="Electronics", available=True),
        Product(name="Phone", category="Electronics", available=False)
    ])
    session.commit()

    # Act: Find available products
    available_products = session.query(Product).filter_by(available=True).all()

    # Assert: Ensure only available products are retrieved
    assert len(available_products) == 1
    assert available_products[0].name == "Laptop"
