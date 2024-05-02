
# Apple JWT Generator

In order to use Sign In with Apple (or other Apple API services) you need to generate a JWT to authenticate your requests. Unfortunately this isn't straight forward and Apple's documentation isn't super helpful with showing you how to generate a JWT.

> Sign In with Apple authorization via JSON Web Tokens (JWT) for initialization and some API calls. You obtain a key used to create the token when you complete the setup in your Apple Developer account.

This simple Python program should help you generate a JWT you can use for development.

### What is a JWT?
JSON Web Tokens are a method for representing claims securely between two parties. For more information check out [jwt.io](https://jwt.io/introduction/)

## What do you need from Apple?

### 1. [Create a Map/Music ID](https://developer.apple.com/videos/play/wwdc2018/508/?time=155)
You can create the Map ID in the developer portal ([developer.apple.com](https://developer.apple.com)) in the `Certificates, Identifiers & Profiles` tab.

### 2. [Your Key ID](https://developer.apple.com/videos/play/wwdc2018/508/?time=220)
Next you will generate a new key. You will need the ID of this key to generate the JWT.

### 3. [Your Map/Music Private Key](https://developer.apple.com/videos/play/wwdc2018/508/?time=280)
Download the private key. You will only be able to download this once. Save it in a private, safe place. You can open this key file with a text editor and copy the entire contents of the file for inserting into `main.py`.
![Key ID](/images/KeyID.jpg)

### 4. Your Team ID.
You will need this ID to generate your JWT. You can get this under the `Membership` tab on the home page of the developer portal.
![Team ID](/images/TeamID.jpg)


## The Good Stuff
You probably just want an easy way to generate your JWT so you can move on with development. 😉 Fine, here is how you can use this program.

*Note: These directions are for macOS*

### Setup Python Environment
1. Clone this repository - `$ git clone git@github.com:addisonwebb/Apple-JWT-Generator.git`
1. Verify you have Python installed - `$ python --version` *Output will likely be `3.10.13`*
1. Setup a virtual environment - `$ python -m venv venv`
1. Begin using virtual environment - `$ source venv/bin/activate`
1. Install requirements - `$ pip install -r requirements.txt`

### Using the program
1. Copy `.env.example` to `.env` - `$ cp .env.example .env`
1. Update the contents of `.env` with the values for your Team ID, Key ID, and private key. Save the file. (Refer guides above)
2. Back in terminal run the program - `$ dotenv python main.py`

You should see output that looks like the following:
```
fyFhbEciOiJFUzI1NiIsInR5cC16IkpXVCIsImtpZCI6IkNTTFo2QjdNOFoifQ.eyJpc3MiOiJGSjRVQk02Uko3IiwiaWF0IjoxNTMwMDcwMtkyLjMyNQA4OSwiZXhwIjoxNTMwMDcxOTkyLjMyNDA4OX0.uveH2BifavlkJp8KLUPCHC0Eh9C6igaUdA6jIawW0r1wsOo44mNSq53e_bH8ZoB2JcNSqXqYvKVYEREi6S02gq
```

🎉 This is the JWT you use to authenticate requests with Sign In With Apple, MapKit JS, MusicKit JS, etc. 


## Sources:
- [Creating a client secret](https://developer.apple.com/documentation/accountorganizationaldatasharing/creating-a-client-secret)
- [Getting Keys and Creating Tokens](https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens)
- [jwt.io](https://jwt.io)
- [pyjwt](https://github.com/jpadilla/pyjwt/)


