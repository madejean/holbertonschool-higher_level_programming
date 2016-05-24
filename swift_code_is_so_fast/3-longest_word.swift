func longest_word(text: String) -> (String){
   var longest = ""
   var word = ""
   var length = 0
   var max = 0
  
for char in text.characters {
   if char == " "  {
    if length > max {
        max = length
        longest = word
   }	   
    word = ""
    length = 0
    } else {
        word += "\(char)"
      	length += 1
   	}
  }
  return longest
}