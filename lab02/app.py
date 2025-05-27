
from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher


app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Route for Caesar cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route for encryption
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route for decryption
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# Route for vigenere cipher page
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

# Route for encryption
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route for decryption
@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

##########################
# Route for PLAYFAIR cipher page
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    
    key = int(request.form['inputKeyPlain'])
    
    playfair = PlayFairCipher()
    encrypted_text = playfair.playfair_creatematrix( key)
    
    return f"<br/>key: {key}<br/>encrypted matrix: {encrypted_text}"

# Route for encryption
@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    playfair = PlayFairCipher()
    encrypted_text = playfair.playfair_encrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route for decryption
@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    playfair = PlayFairCipher()
    decrypted_text = playfair.playfair_decrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
#############11111

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')



# Route for encryption
@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route for decryption
@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
