
# Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.


class Solution(object):
  def compress(self, chars):
      current = chars[0]
      count = 1
      rm = []
      counting = {}


      # Identifying the duplicate Items 
      # duplicate Items stored in rm
      # number of duplicate items is stored in counting
      for i in range(len(chars)):
          if( current == chars[i] ):
              if ( count == 1 ):
                  count += 1
                  continue
              else:
                  counting[chars[i]] = count
                  rm.append(chars[i])
                  count += 1
          else:
              count = 1
              counting[chars[i]] = count
              current = chars[i+1]

      # Removing the duplicates items
      for i in rm:
          chars.remove(i)

      # Adding the counting number to the respective item
      #new_chars = []
      #for i in chars:
      #    new_chars.append(i)
      #    new_chars.append(counting[i])
      i = 0
      last = len(chars) - 1
      while(True):
            if( i == last ):
                chars.append(counting[chars[i]])
                break
            chars.insert((i+1), counting[chars[i]])
            last += 1
            i += 2


      return chars

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
