from wirpl_books.models.base import Model

# CREATE TABLE IF NOT EXISTS `customer` (
#   `id` int(11) NOT NULL DEFAULT 0,
#   `name` varchar(255) NOT NULL,
#   `address` varchar(255) NOT NULL,
#   `email` varchar(50) DEFAULT NULL,
#   `gender` varchar(20) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


class CustomerModel(Model):
    COLUMN_NAMES = ["id", "name", "address", "email", "gender"]

    def get_all(self):
        self.cursor.execute("SELECT * FROM customer")
        return self.cursor.fetchall()

    def insert(self, id, name, address, email, gender):
        self.cursor.execute(
            "INSERT INTO customer (id, name, address, email, gender) VALUES (%s, %s, %s, %s, %s)",
            (id, name, address, email, gender),
        )
        self._conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM customer WHERE id = %s", (id,))
        self._conn.commit()