class Solution:

    def validIPAddress(self, IP: str) -> str:

        """

        Validates whether the given IP address is a valid IPv4 or IPv6 address.

      

        :param IP: A string containing the IP address to validate.

        :return: A string either "IPv4", "IPv6" or "Neither", denoting the type of IP address.

        """

        if "." in IP:

            return self.validate_ipv4(IP)

        elif ":" in IP:

            return self.validate_ipv6(IP)

        else:

            return "Neither"

  

    def validate_ipv4(self, ip: str) -> str:

        """

        Validates IPv4 addresses.


        :param ip: A string of the IPv4 address to validate.

        :return: "IPv4" if valid, otherwise "Neither".

        """

        segments = ip.split(".")

        if len(segments) != 4:

            return "Neither"

      

        for segment in segments:

            # Check if the segment is a number between 0 and 255

            # and does not have leading zeros

            if not segment.isdigit() or not 0 <= int(segment) <= 255 or (segment[0] == "0" and len(segment) > 1):

                return "Neither"

      

        return "IPv4"

  

    def validate_ipv6(self, ip: str) -> str:

        """

        Validates IPv6 addresses.


        :param ip: A string of the IPv6 address to validate.

        :return: "IPv6" if valid, otherwise "Neither".

        """

        segments = ip.split(":")

        if len(segments) != 8:

            return "Neither"


        for segment in segments:

            # Check if the segment is empty, longer than 4 characters or

            # contains characters which are not hexadecimal digits

            if not segment or len(segment) > 4 or not all(c in '0123456789abcdefABCDEF' for c in segment):

                return "Neither"


        return "IPv6"