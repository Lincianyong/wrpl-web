from wirpl_books.models.base import Model


# CREATE TABLE IF NOT EXISTS `transaction` (
#   `id` int(11) NOT NULL DEFAULT 0,
#   `total_price` decimal(20,6) DEFAULT NULL,
#   `payment_method` varchar(20) NOT NULL,
#   `created_at` datetime NOT NULL,
#   `status` varchar(10) NOT NULL,
#   `customer_id` varchar(40) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


class TransactionModel(Model):
    COLUMN_NAMES = [
        "id",
        "total_price",
        "payment_method",
        "created_at",
        "status",
        "customer_id",
    ]

    def get_all(self):
        self.cursor.execute("SELECT * FROM transaction")
        return self.cursor.fetchall()

    def insert(self, id, total_price, payment_method, created_at, status, customer_id):
        self.cursor.execute(
            "INSERT INTO transaction (id, total_price, payment_method, created_at, status, customer_id) "
            + "VALUES (%s, %s, %s, %s, %s, %s)",
            (id, total_price, payment_method, created_at, status, customer_id),
        )
        self._conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM customer WHERE id = %s", (id,))
        self._conn.commit()
