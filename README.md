# API REST

#### This REST API is designed to manage product orders for users.

#### Users can create, and also choose a product and place the order for that product (there is no order limit).

#### Some routes are protected by authentication with JWT tokens, when you log in, a token is created, that token lasts for 15 minutes.

#### The HTTP methods used are only 'POST' and 'GET', to store and send data.

---

## Controllers Layer
* This layer is divided into 3 files, each of these files contains specific paths from where data will be fetched and sent.

## Data Access Layer
* This layer, also divided into 3 files, is the layer that interacts directly with the data source.

## Database Layer
* This layer contains the database settings such as the engine and session builder, and in the 'get_db.py' file, it contains a method for getting sessions from the database.

## Models Layer
* This layer is divided into 5 files, the files 'admin.py', 'order.py', 'product.py' and 'user.py', contain the model of the tables in the database.

## Schemes Layer
* This layer is divided into 3 files, each of these specific files contains the schema of each entity's data, i.e. the way in which the data will be received and stored.

## Services Layer
* This layer, which acts as an intermediary between the data access layer and the controller layer, is divided into 4 files, one containing the authentication services, the others containing the services of each entity.