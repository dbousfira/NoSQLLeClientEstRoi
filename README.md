<p align="center">
  <h3 align="center">Le client est roi</h3>

  <p align="center">Votre client pour qui vous avez développé la base de données dans le brief "Les pays en chiffre" souhaite faire évoluer sa base de données en NoSQL</p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [MongoDB](https://www.mongodb.com/)

<!-- GETTING STARTED -->
## Getting Started

Copy up and running follow these simple steps.

### Prerequisites

* [MongoDB](https://www.mongodb.com/)

### Installation

1. Install [Robo3t](https://robomongo.org/)

2. Clone the repo

    ```sh
    git clone https://github.com/dbousfira/le-client-est-roi
    ```

3. Create src/.env file and replace infos between <>:

    DB_ADDRESS=mongodb://<localhost>:<port>/<db>

4. Import [CSV file](https://github.com/dbousfira/le-client-est-roi/blob/main/data/population_by_country_2020.csv) on Robo3t

5. Create a conda virtual environment with

    ```sh
    conda create --name <env> --file requirements.txt
    ```

<!-- USAGE EXAMPLES -->
## Usage

* Launch Flask:

    ```sh
    $env:FLASK_APP = "src/main.py"
    flask run
    ```

* créer une fonction qui retourne le pays qui correspond au critère passé en paramètre. Ce paramètre est le nom du pays

    Go to http://127.0.0.1:5000/<country_name>.
    => [France](http://127.0.0.1:5000/France) (http://127.0.0.1:5000/France)

* créer une fonction qui insert un nouveau pays avec des données random (on précise uniquement le pays)

    http://127.0.0.1:5000/<country_name> w/ *method POST* (use Postman for example...).
    => http://127.0.0.1:5000/France

* réaliser une fonction pour retourner les pays qui sont regroupés par 4 tranches (à definir) de densité de population

    Go to [localhost](http://127.0.0.1:5000/).
    Countries are sorted and categorised by quartile.

* mettre la date de l'insertion lors d'une création ou mettre à jour une date de modification lors d'un changement de valeur

    Done when insertion.
