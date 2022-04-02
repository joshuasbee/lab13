##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, Joshua Bee
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
       #self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
        self.alphabet = "N$~O?c/3(0SFsWKJ6 hP\"b^85@H-doT+1}v&p'.MDRU7jgeizY[`#4V9Qnf]u\>)AI*|xyB%Lw!G:aXE2C;Zq_{l<tm,rk="
        #this alphabet includes all the 95 characters but makes it much harder to reverse engineer the cipher
        pass

    def get_author(self):
        return "Joshua Bee"

    def get_cipher_name(self):
        return "Vigenere Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        citation = "https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm \n"
        citation += "Author: someone from Tutorials Point, \"Traditional Ciphers\"\nDate Published: unknown, Google first indexed it 10 years ago\n"
        citation += "https://www.britannica.com/topic/Vigenere-cipher \n"
        citation += "Author: Gustavus J. Simmons, \"Vigenère cipher\"\nDate Published: July 14, 2021"
        return citation

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = """def encrypt(plaintext, key):
  plaintextnum = []
  keynum = []
  //convert plaintext to number array
  for i in range(len(plaintext)):
    plaintextnum[i] = search(plaintext, index) in (alphabet)
  //convert key to number array
  for i in range(len(key)):
    keynum[i] = search(plaintext, index) in (alphabet)
  //encode it!
  cipher[] = []
  for i in range(len(plaintext)):
    cipher[i] = plaintextnum[i] + int(dict[i % len(dict)])
  //convert from number to text
  for i in range(len(cipher)):
    encodedText += alphabet[i]
"""
# The decrypt pseudocode
        pc += """
def decrypt(ciphertext, key):
  //convert key to int array
  keynum = []
  for i in range(len(key)):
    keynum[i] = search(ciphertext, index) in alphabet
  
  //convert ciphertext to int array
  ciphertextnum[] = []
  for i in range(len(ciphertext)):
    ciphertextnum[i] = search(ciphertext, index) in alphabet

  //decode it!
  cipher[] = []
  for i in range(len(ciphertextnum)):
    cipher[i] = int(ciphertextnum[i]) - int(dict[i % len(dict)])

  //convert from number to text
  for i in range(len(cipher)):
    encodedText += alphabet[i]
"""
        return pc

    ##########################################################################
    # ENCRYPT
    # We convert the plaintext to the index values of my defined alphabet above
    # then we do the same with the key, then we encode those numbers to other
    # numbers shifting by an amount defined by the key for each letter, 
    # then converting those numbers to text encoded. 
    ##########################################################################
    def encrypt(self, plaintext, password):
        ciphertext = ""
        plaintextnum = []
        keynum = []    
        ciphertextnum = []
        #convert plaintext to numbers
        for i in range(len(plaintext)):
          plaintextnum.insert(i, self.alphabet.index(plaintext[i]))
        #convert key to numbers
        for i in range(len(password)):
          keynum.insert(i, self.alphabet.index(password[i]))
        #convert plaintext numbers to ciphertext numbers
        for i in range(len(plaintextnum)):
          ciphertextnum.insert(i, (int(plaintextnum[i]) + int(keynum[i % len(keynum)])) % len(self.alphabet))
        #convert ciphertext numbers to characters
        for i in range(len(ciphertextnum)):
          ciphertext += self.alphabet[ciphertextnum[i]]
        return ciphertext

    ##########################################################################
    # DECRYPT
    # First we convert the key to numbers used my alphabet defined in init, 
    # then we convert the ciphertext in the same way, then we turn the
    # ciphertext numbers into decoded numbers and into regular text and
    # return it
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ""
        ciphertextnum = []
        keynum = []
        plaintextnum = []
        #convert the key to numbers
        for i in range(len(password)):
          keynum.insert(i, self.alphabet.index(password[i]))
        #convert ciphertext to numbers
        for i in range(len(ciphertext)):
          ciphertextnum.insert(i, self.alphabet.index(ciphertext[i]))
        #convert ciphertext numbers to regular readable text 
        for i in range(len(ciphertextnum)):
          plaintext += self.alphabet[int(ciphertextnum[i]) - int(keynum[i % len(keynum)])]
        return plaintext
# c = Cipher()
# tests = ["lowercase", "password",
#          "UPPERCASE", "PASSWORD",
#          "I am just \"plain\" text ~ 12345", "P@55w0rd!~"]
# for i in range(len(tests)-1):
#   ciphertext = c.encrypt(tests[i], tests[i+1])
#   decryption = c.decrypt(ciphertext, tests[i+1])
#   print(f"""
# ------------------------
#   text: {tests[i]}
#   ciphertext: {ciphertext}
#   decrypted: {decryption}
#   Worked: {tests[i] == decryption}
# ------------------------""", end='')