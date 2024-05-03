class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        This function finds the maximum number of envelopes that can fit inside other envelopes
        like Russian dolls (one envelope fits entirely inside another).

        Args:
            envelopes: A list of lists, where each inner list represents an envelope's width (w)
                       and height (h) as [w, h].

        Returns:
            The maximum number of envelopes that can fit inside each other.
        """

        # Sort the envelopes by width in ascending order and by height in descending order.
        # This ensures that we consider wider envelopes first and prioritize fitting taller envelopes
        # within them.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Create an empty list to store the heights of the envelopes in the current "fitting" sequence.
        LIS = []
        # Initialize the size of the sequence to 0.
        size = 0

        # Iterate through each envelope in the sorted list.
        for (w, h) in envelopes:
            # If the current envelope's height is greater than all heights in the sequence,
            # it can be directly appended as the new "end" of the sequence.
            if not LIS or h > LIS[-1]:
                LIS.append(h)
                size += 1
            else:
                # Otherwise, we need to find the appropriate position in the sequence to insert
                # the current envelope's height while maintaining the increasing order.
                # This is done using binary search.
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if LIS[m] < h:
                        # If the current height is greater than the middle element, search in the right half.
                        l = m + 1
                    else:
                        # If the current height is less than or equal to the middle element,
                        # we've found the appropriate position (or the leftmost position where it's greater).
                        r = m

                # Update the element at the found position with the current envelope's height.
                LIS[l] = h

        # The size of the LIS (Length of Increasing Subsequence) represents the maximum number of envelopes
        # that can fit inside each other.
        return size