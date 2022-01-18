//Name - Jinesh Jain
//Roll No. - 18075069
//Branch - CSE(B.Tech.)
//Subject - Network Security
//Practical Assignment - 0

const plainText = document.getElementById("plainText");
const cipherText = document.getElementById("cipherText");

// Atbash cipher 
// enchipher/decipher in a manner so that-
// A,B,C,...,Z replaced by Z,Y,X,...,A and
// a,b,c,...,z replaced by z,y,x,...,a
// Character other than english alphabets remains unchanged
function cipher(text){
  let output = "";

  //create empty dictionary named "hash" for storing hash values 
  let hash = {}; 

  //Add key-value for uppercase alphabets
  for(let k=65;k<=90;k++) hash[String.fromCharCode(k)] = String.fromCharCode(90-(k-65));

  //Add key-value for lowercase alphabets
  for(let k=97;k<=122;k++) hash[String.fromCharCode(k)] = String.fromCharCode(122-(k-97));

  //obtain required output text using hash
  for(let i=0; i<text.length; i++){
    if(hash[text[i]]) output+=hash[text[i]];
    else output+=text[i];
  }
  return output;
}

//generate cipher text from plain text
function encryption(){
  let text = plainText.value;
  cipherText.value = cipher(text);
}

//obtain plain text from cipher text
function decryption() {
  let text = cipherText.value;
  plainText.value = cipher(text);
}
