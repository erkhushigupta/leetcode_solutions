from typing import List

from math import inf


class Solution:

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        # Extract the x-coordinates from the points

        x_coords = [x for x, _ in points]

      

        # Get the number of points

        num_points = len(x_coords)

      

        # Find the minimum and maximum x-coordinates

        min_coord, max_coord = min(x_coords), max(x_coords)

      

        # Calculate the bucket size based on the range of x-coordinates and number of points

        bucket_size = max(1, (max_coord - min_coord) // (num_points - 1))

      

        # Determine the number of buckets required

        bucket_count = (max_coord - min_coord) // bucket_size + 1

      

        # Initialize buckets, each will hold the minimum and maximum x-coordinates for that bucket

        buckets = [[inf, -inf] for _ in range(bucket_count)]

      

        # Distribute x-coordinates into buckets

        for x in x_coords:

            index = (x - min_coord) // bucket_size

            buckets[index][0] = min(buckets[index][0], x)  # Update min for the bucket

            buckets[index][1] = max(buckets[index][1], x)  # Update max for the bucket

      

        # Variable to keep track of maximum width of vertical area between points

        max_width = 0

      

        # Variable to keep track of the previous bucket's max x-coordinate

        prev_max = inf

      

        # Calculate the maximum width by considering the gaps between the buckets

        for bucket_min, bucket_max in buckets:

            # Ignore empty buckets

            if bucket_min > bucket_max:

                continue

            # Update maximum width if current gap is larger than what we have seen before

            max_width = max(max_width, bucket_min - prev_max)

            # Update previous bucket's max for the next iteration

            prev_max = bucket_max

      

        # Return the maximum width of vertical area found

        return max_width
