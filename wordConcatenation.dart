
// Hi, here's your problem today. This problem was recently asked by LinkedIn:

// Given a set of words, find all words that are concatenations of other words in the set.


// Solution :  ['catsdog', 'dogcat', 'dogcatrat']



main() {
  
  List<String> input = ['rat', 'cat', 'cats', 'dog', 'catsdog', 'dogcat', 'dogcatrat'];
  
  print(Solution().findAllConcatenatedWord(input));
}

class Solution {
  
  List<String> findAllConcatenatedWord(List<String> myList){
    List<String> result = List();
    myList.forEach((element){
      int count = 0;
      myList.forEach((e){
        if(element.contains(e)){
          count += 1;
        }
      });
      if(count > 2){
        result.add(element);
      }
    });
    return result;
  }
  
}

