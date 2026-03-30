# Köpük Naz Handbook

## Description
The Köpük Naz Handbook is a full-stack web application built to celebrate and document the life of Köpük Naz. It features a beautifully styled, interactive frontend and a robust Python backend powered by **Flask**. The application includes a subscription system that saves user emails to a **MongoDB** database and automatically sends out a welcome email via an SMTP service. Additionally, the API is documented using Swagger.

## Tech Stack
* **Backend:** Python, Flask
* **Database:** MongoDB (via PyMongo)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **API Documentation:** Flasgger (Swagger UI)
* **Email Service:** Python `smtplib` and `email.mime`

## Key Features
* **Interactive Slideshow:** The `/basics` page includes a custom JavaScript-powered image slider that details the growth and development of Köpük Naz.
* **Subscription System:** Users can sign up for updates on the landing page (`/butet`). Submitting the form sends a `POST` request to the backend.
* **Automated Emails:** Upon subscribing, the application uses a custom email service to immediately send a notification email via Gmail's SMTP server.
* **Database Integration:** Subscriber emails are permanently stored in a local MongoDB database (`mydatabase`, inside the `email` collection).

## Getting Started

### Prerequisites
To run this project locally, you will need:
* **Python 3.x** installed on your machine.
* **MongoDB** installed and running locally on port `27017` with authentication configured (username: `admin`, password: `password`).

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/BuketVrci/personal-website.git](https://github.com/BuketVrci/personal-website.git)
   cd personal-website
