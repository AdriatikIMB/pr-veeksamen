CREATE TABLE IF NOT EXISTS test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
)



CREATE TABLE IF NOT EXISTS timelister (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prosjekt VARCHAR(255) NOT NULL,
    arbeidsleder VARCHAR(255) NOT NULL,
    prosent INT NOT NULL,
    timer INT NOT NULL,
    type_timer VARCHAR(50) NOT NULL
);
