/* 
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc"; 
const expected4 = "bbcc";

function encodeStr(str) {
  // SETUP
    var newStr = ""
    var counter = 0
    for (var i = 0; i < str.length; i++){
        while (str[i] === str[i]){
            if (str[i] === str[i+i]){
                counter+= 1
            }
            return counter
        }
        str.push([i+counter])
    }

  // WORK
  // RETURN
}

console.log(encodeStr(str1))
/*****************************************************************************/

/* 
    String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

function decodeStr(str) {
  // SETUP
  // WORK
  // RETURN
}