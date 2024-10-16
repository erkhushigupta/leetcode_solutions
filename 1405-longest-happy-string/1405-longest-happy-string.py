from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Initialize a max-heap to store the frequency and characters. 
        # Use negative frequency for max heap since Python has min-heap implementation by default
        max_heap = []
      
        # Add frequencies and characters to heap if they are greater than zero
        if a > 0:
            heappush(max_heap, [-a, 'a'])
        if b > 0:
            heappush(max_heap, [-b, 'b'])
        if c > 0:
            heappush(max_heap, [-c, 'c'])

        # Initialize a list to construct the answer
        result = []
      
        # Continue until the heap is empty
        while max_heap:
            current_char = heappop(max_heap)
          
            # Check if the last two characters in the result are the same as the current one
            if len(result) >= 2 and result[-1] == current_char[1] and result[-2] == current_char[1]:
                # If there are no other characters, break the loop to avoid having three consecutive characters
                if not max_heap:
                    break
                  
                # Get the next character from the heap
                next_char = heappop(max_heap)
              
                # Add the next character to the result and decrease its frequency
                result.append(next_char[1])
                if -next_char[0] > 1:
                    next_char[0] += 1
                    heappush(max_heap, next_char)
              
                # Push the current character back onto the heap for future processing
                heappush(max_heap, current_char)
            else:
                # Add the current character to the result and decrease its frequency
                result.append(current_char[1])
                if -current_char[0] > 1:
                    current_char[0] += 1
                    heappush(max_heap, current_char)

        # Join the list of characters to form the final string and return it
        return ''.join(result)